
package com.mycompany.finalfxml;

import javafx.collections.FXCollections;
import javafx.collections.ObservableList;

public class DataBase {
    public ObservableList<Product> myProducts;

    public DataBase() {
        myProducts = FXCollections.observableArrayList();
    }

    public ObservableList<Product> getProducts() {
        return myProducts;
    }
}

