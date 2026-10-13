<?php
session_start();
require __DIR__ . '/db.php';

$username = $_POST['username'] ?? '';
$password = $_POST['password'] ?? '';

$result = mysqli_query($conn, "SELECT id, password_hash FROM users WHERE username = '$username'");
$user = mysqli_fetch_assoc($result);

if ($user && password_verify($password, $user['password_hash'])) {
    $_SESSION['user_id'] = $user['id'];
    header('Location: /dashboard.php');
    exit;
}
echo 'Invalid login';
