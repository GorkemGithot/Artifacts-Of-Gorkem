

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.finalfxml;

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


