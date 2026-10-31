const express = require('express');
const mysql = require('mysql2');

const app = express();
const db = mysql.createPool({ host: 'localhost', user: 'shop', database: 'shop' });

app.get('/products/:id', (req, res) => {
  db.query(`SELECT id, name, price FROM products WHERE id = ${req.params.id}`, (err, rows) => {
    if (err) return res.status(500).end();
    res.json(rows[0]);
  });
});
