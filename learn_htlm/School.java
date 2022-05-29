class School{
    public methods name(){
        System.out.println("Dodoma High School");
    }
}

class Student extends School{
    public static void main(String[]){
        School obj = new School();
        obj.name();
    }
}