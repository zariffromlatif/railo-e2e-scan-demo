package com.acme.catalog;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;

public class App {
    public boolean inStock(Connection conn, String sku) throws SQLException {
        ResultSet rs = conn.createStatement().executeQuery("SELECT quantity FROM inventory WHERE sku = '" + sku + "'");
        return rs.next() && rs.getInt("quantity") > 0;
    }
}
