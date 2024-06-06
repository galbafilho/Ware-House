const nodemailer = require('nodemailer');

let transporter = nodemailer.createTransport({
  service: 'smtp-relay.sendinblue.com',
  auth: {
    user: 'warehousegwa@gmail.com',
    pass: 'IJTzV92NB3Ubkg5C'
  }
});

// Configurações do e-mail
let mailOptions = {
  from: 'warehousegwa@gmail.com',
  to: 'galbafilho8@gmail.com',
  subject: 'Valdirrrrrrrr',
  text: 'doido'
};

// Envie o e-mail
transporter.sendMail(mailOptions, function(error, info){
  if (error) {
    console.log(error);
  } else {
    console.log('E-mail enviado: ' + info.response);
  }
});

