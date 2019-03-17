<?php 
	session_start();

	// variable declaration
	$firstname ="";
	$lastname = "";
	$username = "";
	$email    = "";
	$errors = array(); 
	$_SESSION['success'] = "";

	// connect to database
	$dbServername = 'localhost';
	$dbUsername = 'root';
	$dbPassword = '';
	$db = 'data';

	$conn = mysqli_connect($dbServername,$dbUsername,$dbPassword,$db);
	// REGISTER USER
	if (isset($_POST['reg_user'])) {
		// receive all input values from the form
		$username = mysqli_real_escape_string($conn, $_POST['Admin_aid']);
		$password = mysqli_real_escape_string($conn, $_POST['Admin_pwd']);
		
		// form validation: ensure that the form is correctly filled
		if (empty($username)) { array_push($errors, "Username is required"); }
		if (empty($password)) { array_push($errors, "Password is required"); }

		
		// register user if there are no errors in the form
		if (count($errors) == 0) {
		
			$query = "INSERT INTO login (username,password) 
					  VALUES('$username', '$2y$10$4REfvTZpxLgkAR/lKG9QiOkSdahOYIR3MeoGJAyiWmRkEFfjH3396');";
					  //$sql = "INSERT INTO admin (Admin_first, Admin_last,Admin_email,Admin_aid,Admin_pwd) VALUES ('$first','$last','$email','$aid','$hashed_pwd');";
			mysqli_query($conn, $query);

			
		}

	}

	// ... 

	// LOGIN USER
	

?>