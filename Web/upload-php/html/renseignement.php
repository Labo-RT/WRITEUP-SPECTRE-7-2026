<?php

$uploadOk = false;
$message = "";

if (!is_dir("uploads/")) {
    mkdir("uploads/", 0777, true);
}

if (isset($_POST["submit"]) && isset($_FILES["fileToUpload"])) {

  $target_dir = "uploads/";
  $target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
  $imageFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));

  $check = false;
  if (isset($_FILES["fileToUpload"]["tmp_name"]) && $_FILES["fileToUpload"]["tmp_name"]) {
    $check = getimagesize($_FILES["fileToUpload"]["tmp_name"]);
  }

  if($imageFileType != "jpg" && $imageFileType != "png" && $imageFileType != "jpeg" && $imageFileType != "gif" ) {
    $message .= "Sorry, only JPG, JPEG, PNG & GIF files are allowed.";
    $uploadOk = false;
  }else {
    $message .= "File is an image - " . ".<br>";
    $uploadOk = true;
  }

  if (file_exists($target_file)) {
    $message .= "Sorry, file already exists.<br>";
    $uploadOk = false;
  }


  if ($uploadOk && move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
        $message .= "The file " . htmlspecialchars(basename($_FILES["fileToUpload"]["name"])) . " has been uploaded.<br>" . "You can check your image in /uploads";
    } elseif ($uploadOk) {
        $message .= "Sorry, there was an error uploading your file.";
    }

}   

?>



<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Spectre-7 — Renseignements Visuels</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="./css/style.css">
</head>

<body class="bg-dark text-light">
  <header class="header d-flex justify-content-between align-items-center px-4 py-2 border-bottom border-secondary">
    <div class="d-flex align-items-center">
        <img src="./images/logo.png" class="spectre-logo me-3">
        <h1 class="h5 mb-0">Spectre-7 — Renseignements Visuels</h1>
    </div>
    <div class="text-muted small">Classification: TOP SECRET // NOFORN</div>
    <button class="btn btn-primary" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasScrolling" aria-controls="offcanvasScrolling">List pages</button>

    <div class="offcanvas offcanvas-start text-bg-dark" data-bs-scroll="true" data-bs-backdrop="false" tabindex="-1" id="offcanvasScrolling" aria-labelledby="offcanvasScrollingLabel">
      <div class="offcanvas-header">
        <h5 class="offcanvas-title" id="offcanvasScrollingLabel">Menu</h5>
        <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
      </div>
      <div class="offcanvas-body">
          <ul>
              <li><a href="./status.html">Status</a></li>
              <li><a href="./renseignement.php">Renseignement</a></li>
              <li><a href="./attack.html">Attack</a></li>
        </ul>
      </div>
    </div>
  </header>

    <main class="container py-5">
        
        <div class="row mb-5">
            <div class="col-12">
                <div class="upload-zone card bg-black border-secondary border-3 p-5 text-center position-relative overflow-hidden">  
                    <i class="fas fa-images fa-4x mb-3 text-success d-block"></i>
                    <h3 class="mb-3">Nouvel Asset Visuel</h3>
                    <p class="mb-4 text-muted">Glissez-déposez ou cliquez pour uploader (JPEG/PNG max 5MB)</p>
                    <form method="post" action="" enctype="multipart/form-data">
                      
                      <input type="file" name="fileToUpload" id="fileToUpload" class="d-none" accept="image/*" multiple>
                      <label for="fileToUpload" class="btn btn-success btn-lg px-5 py-3 fw-bold" name="fileToUpload">
                        <i class="fas fa-plus-circle me-2"></i>UPLOAD ARTEFACT
                      </label>

                      <input type="submit" value="Send" name="submit">
                    
                    </form>

                    <div class="mt-3 small text-muted">
                        <div class="drop-zone" id="dropZone">Zone de drop active</div>
                    </div>
                    <?php if ($message): ?>
                    <div class="alert alert-info mt-3 p-3"><?= nl2br($message) ?></div>
                    <?php endif; ?>
                </div>
            </div>
        </div>

        <!-- Galerie images -->
        <div class="challenge-box">
            <h2 class="challenge-title mb-4">Galerie Renseignements — Cellules Opérationnelles</h2>
            
            <div class="row g-3 gallery-grid" id="galleryGrid">
                <!-- Images exemples (remplace par tes ./images/) -->
                <div class="col-md-3 col-sm-4 col-6">
                    <div class="gallery-item card bg-black border-secondary h-100 overflow-hidden position-relative">
                        <img src="./images/nmap.PNG" class="card-img-top w-100" alt="OSINT Target 01" style="height: 200px; object-fit: cover;">
                        <div class="card-body p-2 small">
                            <h6 class="mb-1">OSINT-Target-01</h6>
                            <span class="badge bg-success">Recon 2026-04-01</span>
                        </div>
                    </div>
                </div>

                <div class="col-md-3 col-sm-4 col-6">
                    <div class="gallery-item card bg-black border-secondary h-100 overflow-hidden position-relative">
                        <img src="./images/msfconsole.png" class="card-img-top w-100" alt="Exploit PoC" style="height: 200px; object-fit: cover;">
                        <div class="card-body p-2 small">
                            <h6 class="mb-1">Exploit-PoC-NEX07</h6>
                            <span class="badge bg-warning">ForgeMalware</span>
                        </div>
                    </div>
                </div>

                <div class="col-md-3 col-sm-4 col-6">
                    <div class="gallery-item card bg-black border-secondary h-100 overflow-hidden position-relative">
                        <img src="./images/grafana.png" class="card-img-top w-100" alt="C2 Dashboard" style="height: 200px; object-fit: cover;">
                        <div class="card-body p-2 small">
                            <h6 class="mb-1">C2-Dashboard-Live</h6>
                            <span class="badge bg-info text-dark">ShadowPulse</span>
                        </div>
                    </div>
                </div>

                <div class="col-md-3 col-sm-4 col-6">
                    <div class="gallery-item card bg-black border-secondary h-100 overflow-hidden position-relative">
                        <img src="./images/kuma.png" class="card-img-top w-100" alt="Malware Sample" style="height: 200px; object-fit: cover;">
                        <div class="card-body p-2 small">
                            <h6 class="mb-1">ForgeMalware-Sample</h6>
                            <span class="badge bg-danger">DOWN (timeout)</span>
                        </div>
                    </div>
                </div>

                <!-- Ajoute plus d'images comme ça -->
                <div class="col-md-3 col-sm-4 col-6">
                    <div class="gallery-item card bg-black border-secondary h-100 text-center p-4">
                        <i class="fas fa-plus fa-3x text-muted mb-2"></i>
                        <p class="small text-muted mb-0">Plus d'assets à venir</p>
                    </div>
                </div>
            </div>

            <div class="text-center mt-4">
                <a href="./controle.html" class="btn btn-outline-secondary">← Retour Control</a>
            </div>
        </div>

    </main>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>

</body>
</html>
