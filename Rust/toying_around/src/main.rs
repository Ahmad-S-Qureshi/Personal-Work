mod number_manipulator;
use number_manipulator::NumberManipulator;
use crate::number_manipulator::CanAdd;

fn main() {
    let mut manipulator = NumberManipulator::new(5, 6, 7);
    println!("{} + {} = {}", manipulator.num1, manipulator.num2, manipulator.num3);
    manipulator.num3 = manipulator.add(manipulator.num1, manipulator.num2);
    println!("{} + {} = {}", manipulator.num1, manipulator.num2, manipulator.num3);
}
