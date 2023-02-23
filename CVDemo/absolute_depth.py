import cv2
import torch
import numpy as np
import matplotlib.pyplot as plt
import open3d as o3d

MODEL_TYPE = "DPT_Hybrid"
# temp = cv2.VideoCapture(0)  # Occupy laptop camera to get other 2 cameras.
LEFT_CAMERA_ID = 1
RIGHT_CAMERA_ID = 2
NUM_RANDOM_POINTS = 100  # Number of random points to use to find midas to disparity conversion.

def main():
    left_camera, right_camera = load_cameras()
    sm_L_x, sm_L_y, sm_R_x, sm_R_y, q, intrinsic = load_calibration_data()
    stereo = create_stereo()
    torch_device = get_torch_device()
    midas = get_midas(torch_device)
    midas_transform = get_midas_transform()
    camera_intrinsic_o3d = get_camera_intrinsic_o3d(intrinsic)
    visualizer = create_visualizer()
    while True:
        left_img, right_img = read_cameras(left_camera, right_camera)
        left_img, right_img = apply_calibration(left_img, right_img,
                                                sm_L_x, sm_L_y, sm_R_x, sm_R_y)
        nn_input = get_nn_input(left_img, midas_transform, torch_device)
        with torch.no_grad():  # We are inferencing only, no need gradients.
            nn_output = midas(nn_input)
            midas_depth_map = get_midas_depth_map(nn_output, left_img)
        left_img_colored = cv2.cvtColor(left_img, cv2.COLOR_BGR2RGB)
        left_img, right_img = cvt_to_gray(left_img, right_img)
        show_combined_imgs(left_img, right_img)
        disparity = stereo.compute(left_img, right_img)
        disparity[disparity < 0] = 0
        cv2.imshow("Disparity", cv2.resize(normalize_array(disparity), None,
                                           fx=0.5, fy=0.5))
        cv2.imshow("MiDaS", cv2.resize(midas_depth_map, None,
                                       fx=0.5, fy=0.5))
        midas_disparity = cvt_midas_to_disparity(midas_depth_map, disparity)
        midas_disparity[midas_disparity <= 0] = 1
        depth = 1 / midas_disparity * 65535  # 65535 is uint16's max value.
        color_map = cv2.applyColorMap((midas_depth_map * 255).astype(np.uint8),
                                      cv2.COLORMAP_JET)
        render_vector_space(left_img_colored, depth, camera_intrinsic_o3d,
                            visualizer)
        # render_vector_space(color_map, depth, camera_intrinsic_o3d,
        #                     visualizer)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

def load_cameras():
    # left_camera = cv2.VideoCapture(LEFT_CAMERA_ID)
    # right_camera = cv2.VideoCapture(RIGHT_CAMERA_ID)
    # left_camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    # left_camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    # right_camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    # right_camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    # return left_camera, right_camera
    return None, None

def load_calibration_data():
    cal_file = cv2.FileStorage()
    cal_file.open("stereoMap.xml", cv2.FileStorage_READ)
    stereo_map_L_x = cal_file.getNode("stereoMapL_x").mat()
    stereo_map_L_y = cal_file.getNode("stereoMapL_y").mat()
    stereo_map_R_x = cal_file.getNode("stereoMapR_x").mat()
    stereo_map_R_y = cal_file.getNode("stereoMapR_y").mat()
    q = cal_file.getNode("q").mat()
    intrinsic_file = cv2.FileStorage()
    intrinsic_file.open("cameraIntrinsic.xml", cv2.FileStorage_READ)
    intrinsic = intrinsic_file.getNode("intrinsic").mat()
    return (stereo_map_L_x, stereo_map_L_y, stereo_map_R_x, stereo_map_R_y, q,
            intrinsic)

def create_stereo():
    stereo = cv2.StereoBM_create()
    stereo.setPreFilterSize(9)
    stereo.setPreFilterCap(31)
    stereo.setMinDisparity(0)
    stereo.setUniquenessRatio(90)
    stereo.setTextureThreshold(90)
    stereo.setSpeckleWindowSize(0)
    stereo.setSpeckleRange(0)
    stereo.setNumDisparities(512)
    stereo.setBlockSize(9)
    return stereo

def read_cameras(left_cam, right_cam):
    # _, left_img = left_cam.read()
    # _, right_img = right_cam.read()
    combined_img = cv2.imread("1676068622.jpg")
    left_img = combined_img[:, :1920, :]
    right_img = combined_img[:, 1920:, :]
    return left_img, right_img

def apply_calibration(left_img, right_img, sm_L_x, sm_L_y, sm_R_x, sm_R_y):
    left_img = cv2.remap(left_img, sm_L_x, sm_L_y,
                         cv2.INTER_LANCZOS4, cv2.BORDER_CONSTANT, 0)
    right_img = cv2.remap(right_img, sm_R_x, sm_R_y,
                          cv2.INTER_LANCZOS4, cv2.BORDER_CONSTANT, 0)
    return left_img, right_img

def cvt_to_gray(left_img, right_img):
    left_img = cv2.cvtColor(left_img, cv2.COLOR_BGR2GRAY)
    right_img = cv2.cvtColor(right_img, cv2.COLOR_BGR2GRAY)
    return left_img, right_img

def show_combined_imgs(left_img, right_img):
    combined_img = np.concatenate((left_img, right_img), axis=1)
    combined_img = cv2.resize(combined_img, None, fx=0.5, fy=0.5)
    cv2.imshow("Left and Right Image", combined_img)

def normalize_array(arr):
    max_val = np.max(arr)
    if max_val != 0:
        return arr / max_val
    else:
        return arr

def get_torch_device():
    if torch.cuda.is_available():
        print("Using GPU for PyTorch.")
        return torch.device("cuda")  # Nvidia GPU
    # elif torch.backends.mps.is_available():
    #     print("Using GPU for PyTorch.")
    #     return torch.device("mps")  # Apple GPU
    else:
        print("Using CPU for PyTorch.")
        return torch.device("cpu")  # CPU

def get_midas(device):
    midas = torch.hub.load("intel-isl/MiDaS", MODEL_TYPE)
    midas.to(device)
    midas.eval()
    return midas

def get_midas_transform():
    temp = torch.hub.load("intel-isl/MiDaS", "transforms")
    if MODEL_TYPE == "DPT_Large" or MODEL_TYPE == "DPT_Hybrid":
        return temp.dpt_transform
    else:
        return temp.small_transform

def get_nn_input(image, transform, device):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    nn_input = transform(image).to(device)
    return nn_input

def get_midas_depth_map(nn_output, image):
    nn_output = torch.nn.functional.interpolate(
        nn_output.unsqueeze(1),
        size=image.shape[:2],
        mode="bicubic",
        align_corners=False,
    ).squeeze()
    depth_map = nn_output.cpu().numpy()
    depth_map = cv2.normalize(depth_map, None, 0, 1,
                              norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_64F)
    return depth_map

def cvt_midas_to_disparity(midas, disparity):
    nonzero_indices = np.argwhere(disparity != 0)
    picked_indices = np.random.choice(len(nonzero_indices),
                                      size=NUM_RANDOM_POINTS)
    nonzero_indices = nonzero_indices[picked_indices]
    nonzero_indices = (nonzero_indices[:, 0], nonzero_indices[:, 1])
    x = midas[nonzero_indices]
    y = disparity[nonzero_indices]
    plt.plot(x, y, "o")
    m = find_best_fit(x, y)
    plt.plot([0, 1], [0, m])
    plt.xlim(0, 1)
    plt.ylim(0, 10000)
    plt.pause(0.01)
    plt.clf()
    return m * midas

def find_best_fit(x, y):
    X = x.reshape((NUM_RANDOM_POINTS, 1))
    y = y.reshape((NUM_RANDOM_POINTS, 1))
    # Calculate theta using the normal equation.
    theta = np.matmul(np.matmul(np.linalg.inv(np.matmul(X.T, X)), X.T), y)
    m = theta[0][0]
    return m

def get_camera_intrinsic_o3d(intrinsic):
    camera_intrinsic_o3d = o3d.camera.PinholeCameraIntrinsic(
        width=960, height=540,
        fx=intrinsic[0][0], fy=intrinsic[1][1],
        cx=intrinsic[0][2], cy=intrinsic[1][2])
    return camera_intrinsic_o3d

def create_visualizer():
    visualizer = o3d.visualization.Visualizer()
    visualizer.create_window(width=1280, height=720)
    # Add 2 points so that bounding box is not all zeros.
    two_points = o3d.geometry.PointCloud()
    two_points.points = o3d.utility.Vector3dVector([
        (-2.5, -0.5, -3),
        ( 2.5,  0.5,  0.1),
    ])
    visualizer.add_geometry(two_points)
    # Zoom in.
    visualizer_control = visualizer.get_view_control()
    visualizer_control.set_zoom(0.1)
    # Draw axes.
    visualizer.add_geometry(
                   o3d.geometry.TriangleMesh.create_coordinate_frame(size=0.1))
    return visualizer

def render_vector_space(color, depth, camera_intrinsic_o3d, visualizer):
    # color[:] = 0  # No color mode.
    # Scale down images by factor of 4.
    color = color[::2, ::2]
    depth = depth[::2, ::2]
    # Create rgbd image.
    color_info = o3d.geometry.Image(color.astype(np.uint8))
    depth_info = o3d.geometry.Image(depth.astype(np.uint16))
    rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(color_info,
                                                                    depth_info,
                                                convert_rgb_to_intensity=False)
    point_cloud = o3d.geometry.PointCloud.create_from_rgbd_image(rgbd_image,
                                                          camera_intrinsic_o3d)
    point_cloud.transform([[1, 0, 0, 0], [0, -1, 0, 0],
                           [0, 0, -1, 0], [0, 0, 0, 1]])
    # Get min and max points of point_cloud.
    # point_cloud_data = np.asarray(point_cloud.points)
    # print(np.min(point_cloud_data, axis=0))
    # print(np.max(point_cloud_data, axis=0))
    visualizer.add_geometry(point_cloud, reset_bounding_box=False)
    visualizer.poll_events()
    visualizer.run()  # Picture mode.
    visualizer.remove_geometry(point_cloud, reset_bounding_box=False)

if __name__ == "__main__":
    main()
