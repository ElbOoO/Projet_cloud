const AWS = require('aws-sdk');


// INITIALISATION DU BUCKET S3 AWS
AWS.config.region = 'us-east-1';

AWS.config.credentials = new AWS.Credentials('ASIA2OU3CVNSBYKEAZ6X', 'rjA4SL7IOJLpxxqPMnpOyxwFUaWJEE7hJSQVoVYU', 'FwoGZXIvYXdzEIb//////////wEaDKJqQLKOwOIh63wIwSK6AYPxwo38cSpMlT3dAQiolJpu23Y+5GwHS9WMc5+HSPQkKt57zG+EcKw8cP92Tl3wjsJsmm834y4Tzz1sb/ysCYznOmbpOV3Shsm9c5YtQMF1cXR3GFS1qaMHBicw6Nluk2ffvfmxDs8PbkQ9wZ2uHU6dCsPcNTN5H0Y5hchK3QS3QQvjR3K73YnfBgjKiO/a6jwpZjhY9/T19iW7RO+NYIMKybb/3Pud69euVxcSesV3k2cr+ojLlWpv8Ciht7mMBjItCVNKuriixNS4s4njWeM6b0yLODdhmeP9L0UGUGcG/H4T8gnUD0Rd2EExtPAA');

AWS.config.credentials.get(function(err) {
    if (err) alert(err);
    console.log(AWS.config.credentials);
});

var bucketName = 'projet-hot-dogs';

var bucket = new AWS.S3({
    params: {
        Bucket: bucketName
    }
});


// FONCTIONS POUR UPLOAD DANS LE BUCKET
function upload_jaaj(file) {

    if (file) {
        var params = {
            Key: "logs/" + new Date() + ".txt",
            ContentType: "text/plain",
            Body: file,
            ACL: 'public-read'
        };

        bucket.putObject(params, function(err, data) {
            if (err) {
                console.log(err);
            }
        });
    } else {
        console.log("Rien a upload");
    }
}

async function getNbFichiers(path) {
  const objects = await bucket.listObjects({Prefix: path, Delimiter: '/'}).promise();
  return Number(objects.Contents.length);
}


// FONCTIONS POUR NOTRE PAGE HTML
$(async function(){
    nbImgs = await getNbFichiers('').then(function(result) { return result; });
    $('.fit-picture').each(async function() {
        //nbImgs = await getNbFichiers('').then(function(result) { return result; });
        var num = Math.floor(Math.random() * nbImgs + 1),
            img = $(this);
            if (num>=10) {
                img.attr('src', 'https://projet-hot-dogs.s3.amazonaws.com/im' + num + '.jpg');
                
            }else{
                img.attr('src', 'https://projet-hot-dogs.s3.amazonaws.com/im0' + num + '.jpg');
            }
        img.attr('alt', 'Src: '+img.attr('src'));
    });
    document.getElementById('nomUpload').value = "im" + (nbImgs+1) + ".jpg";
});

window.recordCheckBoxes = () => {
    let box1 = document.getElementById('check1').checked;
    let img1 = document.getElementById('img1').src;
    let box2 = document.getElementById('check2').checked;
    let img2 = document.getElementById('img2').src;
    let box3 = document.getElementById('check3').checked;
    let img3 = document.getElementById('img3').src;
    let box4 = document.getElementById('check4').checked;
    let img4 = document.getElementById('img4').src;

    console.log(img1,box1);
    console.log(img2,box2);
    console.log(img3,box3);
    console.log(img4,box4);
    alert("Votes Submitted");

    var blob = new Blob([img1,"\n",box1,"\n",img2,"\n",box2,"\n",img3,"\n",box3,"\n",img4,"\n",box4], { type: "text/plain;charset=utf-8" });
    upload_jaaj(blob);
}

window.reload = () => {
    window.location.reload();
}