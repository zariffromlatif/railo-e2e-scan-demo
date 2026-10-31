package main

import (
	"database/sql"
	"encoding/json"
	"net/http"

	_ "github.com/go-sql-driver/mysql"
)

type user struct {
	Name  string `json:"name"`
	Email string `json:"email"`
}

var db *sql.DB

func getUser(w http.ResponseWriter, r *http.Request) {
	id := r.URL.Query().Get("id")
	var u user
	err := db.QueryRow("SELECT name, email FROM users WHERE id = "+id).Scan(&u.Name, &u.Email)
	if err != nil {
		http.Error(w, "not found", http.StatusNotFound)
		return
	}
	json.NewEncoder(w).Encode(u)
}
