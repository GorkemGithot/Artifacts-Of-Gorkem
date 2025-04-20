package com.mycompany.finalfxml;

import java.io.IOException;
import javafx.fxml.FXML;
import javafx.scene.control.TextField;

public class PrimaryController {
    @FXML
    public TextField text1=new TextField();
    
    @FXML
    public TextField text2=new TextField();
    
    
    
    @FXML
    private void signIn() throws IOException {
        
        String nameInput=text1.getText();
        String passInput=text2.getText();
        /*if("admin".equals(nameInput) && "1234".equals(passInput)){
            App.setRoot("scene2");
        }
*/
        App.setRoot("scene2");
    }
    @FXML
    private void deleteText1() throws IOException {
        text1.setOnMouseClicked(event -> text1.setText(""));   
    }
    @FXML
    private void deleteText2() throws IOException {
        text2.setOnMouseClicked(event -> text2.setText(""));   
    }
}

