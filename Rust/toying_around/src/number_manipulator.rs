include!("can_add.rs");

pub struct NumberManipulator {
    pub num1: i8,
    pub num2: i8,
    pub num3: i8,
}

impl NumberManipulator {
    pub fn new(number1: i8, number2: i8, number3: i8) -> NumberManipulator {
        NumberManipulator { num1: (number1), num2: (number2), num3: (number3) }
    }
}

impl CanAdd for NumberManipulator{
    
}