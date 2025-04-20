package com.mycompany.projemmmm;

import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.ComboBox;
import javafx.scene.control.Label;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.TextField;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

public class App extends Application {
    Stage window1;
    Scene scene1,scene2,scene3,scene4;

    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage stage) {
        window1 = stage;
        
        TableView table=new TableView<Product>();
        TableColumn nameColumn=new TableColumn<Product,String>("Name");
        nameColumn.setCellValueFactory(new PropertyValueFactory<Product,String>("name"));

        
        TableColumn quantityColumn=new TableColumn<Product,Integer>("Quantity");
        quantityColumn.setCellValueFactory(new PropertyValueFactory<Product,Integer>("quantity"));

        
        TableColumn priceColumn=new TableColumn<Product,Double>("Price");
        priceColumn.setCellValueFactory(new PropertyValueFactory<Product,Double>("price"));
        
        table.getColumns().add(nameColumn);
        table.getColumns().add(quantityColumn);
        table.getColumns().add(priceColumn);
        
        table.setColumnResizePolicy(TableView.CONSTRAINED_RESIZE_POLICY);
        Button button09=new Button("Main Menu");
        button09.setOnAction(event->{
            window1.setScene(scene2);
        });
        VBox layout4=new VBox();
        layout4.setAlignment(Pos.CENTER);
        layout4.getChildren().addAll(table,button09);
        scene4=new Scene(layout4,600,400);
        
        ComboBox<String> nameOfProduct=new ComboBox<>();
        nameOfProduct.getItems().addAll("Laptop","Desktop","Monitor","Printer");
        nameOfProduct.setPromptText("Please choose a product type");
        TextField quantityOfProduct=new TextField("Quantity of Product");
        quantityOfProduct.setOnMouseClicked(event -> quantityOfProduct.setText(""));
        TextField priceOfProduct=new TextField("Price of Product");
        priceOfProduct.setOnMouseClicked(event -> priceOfProduct.setText(""));
        Button buttonforEntry=new Button("Enter the product");
        Button mainMenu=new Button("Main Menu");
        mainMenu.setOnAction(event->{
            window1.setScene(scene2);
        });
        
        buttonforEntry.setOnAction(event->{
            String nameInput=nameOfProduct.getValue();
            int quantityInput = Integer.parseInt(quantityOfProduct.getText());
            double priceInput = Double.parseDouble(priceOfProduct.getText());
            Product my=new Product(nameInput,quantityInput,priceInput);
            table.getItems().add(my);
        });
        Label label2 = new Label("Welcome to the Product Entry System!");
        VBox layout3 = new VBox(20);
        layout3.setAlignment(Pos.CENTER);
        layout3.setPadding(new Insets(20,20,20,20));
        layout3.getChildren().addAll(label2, nameOfProduct,quantityOfProduct,priceOfProduct,buttonforEntry,mainMenu);
        scene3 = new Scene(layout3, 600, 400);

        
        
        Button button2 = new Button("PRODUCT ENTRY SYSTEM");
        button2.setOnAction(e -> window1.setScene(scene3));
        Button button3 = new Button("PRODUCT VIEWER SYSTEM");
        button3.setOnAction(e -> window1.setScene(scene4));
        VBox layout2 = new VBox(30);
        layout2.setAlignment(Pos.CENTER);
        layout2.getChildren().addAll(button2,button3);
        layout2.setPadding(new Insets(20,20,20,20));
        scene2=new Scene(layout2,600,400);
        // İlk sahne (scene1) düzenleme
        Label label1 = new Label("Welcome to the product placer!");
        
        TextField name=new TextField("Name");
        name.setOnMouseClicked(event -> name.setText(""));
        TextField pass=new TextField("SurName");
        pass.setOnMouseClicked(event -> pass.setText(""));
        Button button1 = new Button("SIGN IN");
        button1.setOnAction(event->{
           String nameInput=name.getText();
           String passInput=pass.getText();
           if("admin".equals(nameInput) && "1234".equals(passInput)){
               window1.setScene(scene2); 
           }
           else{
               label1.setText("Your name or password is wrong. Please try again.");
           }
        });
        
        VBox layout1 = new VBox(30);
        layout1.setAlignment(Pos.CENTER);
        layout1.getChildren().addAll(label1,name,pass,button1);
        layout1.setPadding(new Insets(20,20,20,20));
        scene1 = new Scene(layout1, 600, 400);
        
        window1.setScene(scene1);
        window1.setTitle("Scene Switcher");
        window1.show();
    }
}



/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.projemmmm;

import javafx.beans.property.DoubleProperty;
import javafx.beans.property.IntegerProperty;
import javafx.beans.property.SimpleDoubleProperty;
import javafx.beans.property.SimpleIntegerProperty;
import javafx.beans.property.SimpleStringProperty;
import javafx.beans.property.StringProperty;

/**
 *
 * @author internet
 */

public class Product {
        public StringProperty name;
        public IntegerProperty quantity;
        public DoubleProperty price;

        public Product(String name, int quantity, double price) {
            this.name = new SimpleStringProperty(name);
            this.quantity = new SimpleIntegerProperty(quantity);
            this.price = new SimpleDoubleProperty(price);
        }

        public String getName() {
            return name.get();
        }

        public void setName(String name) {
            this.name.set(name);
        }

        public Integer getQuantity() {
            return quantity.get();
        }

        public void setQuantity(Integer quantity) {
            this.quantity.set(quantity);
        }

        public Double getPrice() {
            return price.get();
        }

        public void setPrice(Double price) {
            this.price.set(price);
        }
}


