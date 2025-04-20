
package com.mycompany.finalfxml;

import java.io.IOException;
import javafx.fxml.FXML;

public class SecondaryController {

    @FXML
    private void entryFunc() throws IOException {
        App.setRoot("scene3");
    }

    @FXML
    private void monitorFunc() throws IOException {
        App.setRoot("scene4");
    }
}
