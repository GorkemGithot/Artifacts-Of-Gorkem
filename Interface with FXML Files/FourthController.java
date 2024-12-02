
package com.mycompany.finalfxml;

import java.io.IOException;
import java.net.URL;
import java.util.ResourceBundle;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.cell.PropertyValueFactory;

public class FourthController implements Initializable {

    @FXML
    private TableView<Product> table1;
    
    @FXML
    private Button button;

    @FXML
    private TableColumn<Product, String> nameCol;

    @FXML
    private TableColumn<Product, Integer> quantityCol;

    @FXML
    private TableColumn<Product, Double> priceCol;

    @Override
    public void initialize(URL url, ResourceBundle rb) {
        // Kolonların yapılandırılması
        nameCol.setCellValueFactory(new PropertyValueFactory<>("name"));
        quantityCol.setCellValueFactory(new PropertyValueFactory<>("quantity"));
        priceCol.setCellValueFactory(new PropertyValueFactory<>("price"));
        table1.setItems(App.getDataBase().myProducts);
        
    }

    @FXML
    public void buttonFunc() throws IOException{
        App.setRoot("scene2");
    }
}