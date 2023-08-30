pub trait CanAdd {
    fn add(&self, num1: i8, num2: i8) -> i8 {
        num1+num2
    }
}