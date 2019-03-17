<?php include('server.php') ?>
<!DOCTYPE html>
<html>
<head>
	<title>Registration for Student</title>
	<!--<link rel="stylesheet" type="text/css" href="style.css">-->
</head>
<body>
	<div class="header">
		<h2>Registeration form for student to join lost and found whole class chat</h2>
	</div>
	
	<form method="post" action="register.php">

		<?php include('errors.php'); ?>
		
		<div class="input-group">
			<label>Firstname</label>
			<input type="text" name="Admin_first" value="<?php echo $firstname; ?>">
		</div>



		<div class="input-group">
			<label>Lastname</label>
			<input type="text" name="Admin_last" value="<?php echo $lastname; ?>">
		</div>



		<div class="input-group">
			<label>Username(used to login)</label>
			<input type="text" name="Admin_aid" value="<?php echo $username; ?>">
		</div>
		<div class="input-group">
			<label>Email</label>
			<input type="email" name="Admin_email" value="<?php echo $email; ?>">
		</div>
		<div class="input-group">
			<label>Password</label>
			<input type="password" name="Admin_pwd">
		</div>
		
		<div class="input-group">
			<button type="submit" class="btn" name="reg_user">Register</button>
		</div>
		<br>
		<a href = "login.php">
		Login</a>
	</form>
</body>
</html>