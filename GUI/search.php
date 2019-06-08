
<!DOCTYPE html>
<html>
<?php
header("Cache-Control: no-store, no-cache, must-revalidate, max-age=0");
header("Cache-Control: post-check=0, pre-check=0", false);
header("Pragma: no-cache");
?>


<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat">
<head>
	<title>Result</title>
	<style type="text/css">
		body {
            background-color:#F0FFF0 ;
               
			font-weight: bold;
		
			//margin-left:1%;
			color: black;

		}
		
		{
 	 		box-sizing: border-box;
		}
/* Container for flexboxes */
		section {
  			display: -webkit-flex;
  			display: flex;

		}

/* Style the navigation menu */
		nav {
  			-webkit-flex: 1;
  			-ms-flex: 1;
  			flex: 0.1;
  			background: #99D1D3;
  			padding: 0px;
			}


/* Style the content */
		article {
  			-webkit-flex: 3;
  			-ms-flex: ;
  			flex: 3;
  			background-color: none;
  			padding: 5px;
			}
</style>
	
	<link href="https://fonts.googleapis.com/css?family=Rokkitt" rel="stylesheet">
</head>
<body>
<div style="background-color:#F19373; margin:-1%">
	<h1 style="text-align:left; font-style: italic; font-weight:800; font-size:50px; margin-left:2%">RESULT</h1>
</div>
<section>
 <nav style="margin-right:-0.1%;">
 </nav>
  
  <article>
	<article style="background-color:#99D1D3; margin:-0.4%; font-size:15px">
	<h2 style="font-style: italic; font-size:20px; font-weight:500;">Input Search Term:</h2>
	
	
			<?php

                echo $_POST["searchterm"];
                $myfile = fopen("GUI/uploads/description.txt", "w");
                $term=$_POST["searchterm"];
                fwrite($myfile, $term);
                fclose($myfile);

                $result = exec("python3 /home/duc/Documents/Text-and-Content-Based-Image-Retrieval-master/Predict_bleu_score.py");
	
            ?>
	
	</article>
    <h3 style="margin-left:1%"></h3>
		<?php
		    
		        $dirname = "GUI/uploads/matched-images/";
		        $images = glob($dirname."*.jpg");
		        $inputFile = fopen("GUI/uploads/matched_images.txt", "r");
		        foreach($images as $image) {
		            echo '<img src='.$image.'" height="250px" hspace="20px" vspace="10px"/>';    
		        }
		        fclose($inputFile);
		        
		                
		?>
	
	</article>
</section>
</body>

</html>