import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(imagefirst, imagesecond, imagethird, imageforth,
               textfirst, textsecond, textthird, textforth):
    sender_email = ''
    receiver_email = ''
    password = ''

    message = MIMEMultipart('alternative')
    message['Subject'] = 'Daily Valorant Skin Update'
    message['From'] = sender_email
    message['To'] = receiver_email

    # Create the plain-text and HTML version of your message

    html = """\
    <html>
          <head>
            <!-- Compiled with Bootstrap Email version: 1.1.0 -->
            <meta http-equiv='Content-Type' content='text/html; charset=utf-8'>
            <meta http-equiv='x-ua-compatible' content='ie=edge'>
            <meta name='x-apple-disable-message-reformatting'>
            <meta name='viewport' content='width=device-width, initial-scale=1'>
            <meta name='format-detection' content='telephone=no, date=no, address=no, email=no'>
            <style type='text/css'>
              body,table,td{font-family:Helvetica,Arial,sans-serif !important}.ExternalClass.ExternalClass,.ExternalClass p,.ExternalClass span,.ExternalClass font,.ExternalClass td,.ExternalClass div{line-height:150%}a{text-decoration:none}*{color:inherit}a[x-apple-data-detectors],u+#body a,#MessageViewBody a{color:inherit;text-decoration:none;font-size:inherit;font-family:inherit;font-weight:inherit;line-height:inherit}img{-ms-interpolation-mode:bicubic}table:not([class^=s-]){font-family:Helvetica,Arial,sans-serif;mso-table-lspace:0pt;mso-table-rspace:0pt;border-spacing:0px;border-collapse:collapse}table:not([class^=s-]) td{border-spacing:0px;border-collapse:collapse}@media screen and (max-width: 600px){.max-w-56,.max-w-56>tbody>tr>td{max-width:224px !important;width:100% !important}.max-w-96,.max-w-96>tbody>tr>td{max-width:384px !important;width:100% !important}.w-lg-80,.w-lg-80>tbody>tr>td{width:auto !important}.w-full,.w-full>tbody>tr>td{width:100% !important}.w-32,.w-32>tbody>tr>td{width:128px !important}.pt-4:not(table),.pt-4:not(.btn)>tbody>tr>td,.pt-4.btn td a,.py-4:not(table),.py-4:not(.btn)>tbody>tr>td,.py-4.btn td a{padding-top:16px !important}.pb-4:not(table),.pb-4:not(.btn)>tbody>tr>td,.pb-4.btn td a,.py-4:not(table),.py-4:not(.btn)>tbody>tr>td,.py-4.btn td a{padding-bottom:16px !important}*[class*=s-lg-]>tbody>tr>td{font-size:0 !important;line-height:0 !important;height:0 !important}.s-6>tbody>tr>td{font-size:24px !important;line-height:24px !important;height:24px !important}.s-10>tbody>tr>td{font-size:40px !important;line-height:40px !important;height:40px !important}}
            </style> """ + f""" </head>
          <body style='outline: 0; width: 100%; min-width: 100%; height: 100%; -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family: Helvetica, Arial, sans-serif; line-height: 24px; font-weight: normal; font-size: 16px; -moz-box-sizing: border-box; -webkit-box-sizing: border-box; box-sizing: border-box; color: #000000; margin: 0; padding: 0; border: 0;' bgcolor='#ffffff'>
            <table class='body' valign='top' role='presentation' border='0' cellpadding='0' cellspacing='0' style='outline: 0; width: 100%; min-width: 100%; height: 100%; -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family: Helvetica, Arial, sans-serif; line-height: 24px; font-weight: normal; font-size: 16px; -moz-box-sizing: border-box; -webkit-box-sizing: border-box; box-sizing: border-box; color: #000000; margin: 0; padding: 0; border: 0;' bgcolor='#ffffff'>
              <tbody>
                <tr>
                  <td valign='top' style='line-height: 24px; font-size: 16px; margin: 0;' align='left'>
                    <table class='bg-black w-full' role='presentation' border='0' cellpadding='0' cellspacing='0' style='width: 100%;' bgcolor='#000000' width='100%'>
                      <tbody>
                        <tr>
                          <td style='line-height: 24px; font-size: 16px; width: 100%; margin: 0;' align='left' bgcolor='#000000' width='100%'>
                            <table class='container' role='presentation' border='0' cellpadding='0' cellspacing='0' style='width: 100%;'>
                              <tbody>
                                <tr>
                                  <td align='center' style='line-height: 24px; font-size: 16px; margin: 0; padding: 0 16px;'>
                                    <!--[if (gte mso 9)|(IE)]>
                                    <table align='center' role='presentation'>
                                      <tbody>
                                        <tr>
                                          <td width='600'>
                                            <![endif]-->
                                            <table align='center' role='presentation' border='0' cellpadding='0' cellspacing='0' style='width: 100%; max-width: 600px; margin: 0 auto;'>
                                              <tbody>
                                                <tr>
                                                  <td style='line-height: 24px; font-size: 16px; margin: 0;' align='left'>
                                                    <!--- FIND Me NOW!-->
                                                    <table class='s-10 w-full' role='presentation' border='0' cellpadding='0' cellspacing='0' style='width: 100%;' width='100%'>
                                                      <tbody>
                                                        <tr>
                                                          <td style='line-height: 40px; font-size: 40px; width: 100%; height: 40px; margin: 0;' align='left' width='100%' height='40'>
                                                            &#160;
                                                          </td>
                                                        </tr>
                                                      </tbody>
                                                    </table>
                                                    <table class='ax-center' role='presentation' align='center' border='0' cellpadding='0' cellspacing='0' style='margin: 0 auto;'>
                                                      <tbody>
                                                        <tr>
                                                          <td style='line-height: 24px; font-size: 16px; margin: 0;' align='left'>
                                                            <img class='w-32' src='https://assets.bootstrapemail.com/logos/dark/combined.png' style='height: auto; line-height: 100%; outline: none; text-decoration: none; display: block; width: 128px; border: 0 none;' width='128'>
                                                          </td>
                                                        </tr>
                                                      </tbody>
                                                    </table>
                                                    <table class='s-10 w-full' role='presentation' border='0' cellpadding='0' cellspacing='0' style='width: 100%;' width='100%'>
                                                      <tbody>
                                                        <tr>
                                                          <td style='line-height: 40px; font-size: 40px; width: 100%; height: 40px; margin: 0;' align='left' width='100%' height='40'>
                                                            &#160;
                                                          </td>
                                                        </tr>
                                                      </tbody>
                                                    </table>
                                                    <table class='ax-center' role='presentation' align='center' border='0' cellpadding='0' cellspacing='0' style='margin: 0 auto;'>
                                                      <tbody>
                                                        <tr>
                                                          <td style='line-height: 24px; font-size: 16px; margin: 0;' align='left'>
                                                            <img class='max-w-56  rounded-lg' src='{imagefirst}' style='height: auto; line-height: 100%; outline: none; text-decoration: none; display: block; border-radius: 8px; max-width: 224px; width: 100%; border: 0 none;' width='224'>
                                                          </td>
                                                        </tr>
                                                      </tbody>
                                                    </table>
                                                    <table class='s-10 w-full' role='presentation' border='0' cellpadding='0' cellspacing='0' style='width: 100%;' width='100%'>
                                                      <tbody>
                                                        <tr>
                                                          <td style='line-height: 40px; font-size: 40px; width: 100%; height: 40px; margin: 0;' align='left' width='100%' height='40'>
                                                            &#160;
                                                          </td>
                                                        </tr>
                                                      </tbody>
                                                    </table>
                                                    <table class='ax-center' role='presentation' align='center' border='0' cellpadding='0' cellspacing='0' style='margin: 0 auto;'>
                                                      <tbody>
                                                        <tr>
                                                          <td style='line-height: 24px; font-size: 16px; margin: 0;' align='left'>
                                                            <p class='max-w-96 lh-lg text-white text-center text-2xl' style='line-height: 2; font-size: 24px; color: #ffffff; max-width: 384px; -premailer-width: 384; width: 100%; margin: 0;' align='center'>
                                                              {textfirst}
                                                            </p>
                                                          </td>
                                                        </tr>
                                                      </tbody>
                                                    </table>
                                                    <table class='s-10 w-full' role='presentation' border='0' cellpadding='0' cellspacing='0' style='width: 100%;' width='100%'>
                                                      <tbody>
                                                        <tr>
                                                          <td style='line-height: 40px; font-size: 40px; width: 100%; height: 40px; margin: 0;' align='left' width='100%' height='40'>
                                                            &#160;
                                                          </td>
                                                        </tr>
                                                      </tbody>
                                                    </table>
                                                    <table class='btn btn-yellow-300 rounded-full fw-800 text-5xl py-4 ax-center  w-full w-lg-80' role='presentation' align='center' border='0' cellpadding='0' cellspacing='0' style='border-radius: 9999px; border-collapse: separate !important; width: 320px; font-size: 48px; line-height: 57.6px; font-weight: 800 !important; margin: 0 auto;' width='320'>
                                                      <tbody>
                                                        <tr>
                                                          <td style='line-height: 24px; font-size: 16px; border-radius: 9999px; width: 320px; font-weight: 800 !important; margin: 0;' align='center' bgcolor='#ffda6a' width='320'>
                                                            <a href='https://bootstrapemail.com' style='color: #111111; font-size: 16px; font-family: Helvetica, Arial, sans-serif; text-decoration: none; border-radius: 9999px; line-height: 20px; display: inline-block; font-weight: 800 !important; white-space: nowrap; background-color: #ffda6a; padding: 16px 12px; border: 1px solid #ffda6a;'>Open</a>
                                                          </td>
                                                        </tr>
                                                      </tbody>
                                                    </table>
                                                    <table class='s-10 w-full' role='presentation' border='0' cellpadding='0' cellspacing='0' style='width: 100%;' width='100%'>
                                                      <tbody>
                                                        <tr>
                                                          <td style='line-height: 40px; font-size: 40px; width: 100%; height: 40px; margin: 0;' align='left' width='100%' height='40'>
                                                            &#160;
                                                          </td>
                                                        </tr>
                                                      </tbody>
                                                    </table>
                                                    <table class='s-6 w-full' role='presentation' border='0' cellpadding='0' cellspacing='0' style='width: 100%;' width='100%'>
                                                      <tbody>
                                                        <tr>
                                                          <td style='line-height: 24px; font-size: 24px; width: 100%; height: 24px; margin: 0;' align='left' width='100%' height='24'>
                                                            &#160;
                                                          </td>
                                                        </tr>
                                                      </tbody>
                                                    </table>
                                                    <div class='text-muted text-center' style='color: #718096;' align='center'>
                                                    </div>
                                                    <table class='s-6 w-full' role='presentation' border='0' cellpadding='0' cellspacing='0' style='width: 100%;' width='100%'>
                                                      <tbody>
                                                        <tr>
                                                          <td style='line-height: 24px; font-size: 24px; width: 100%; height: 24px; margin: 0;' align='left' width='100%' height='24'>
                                                            &#160;
                                                          </td>
                                                        </tr>
                                                      </tbody>
                                                    </table>
                                                    <table class='s-10 w-full' role='presentation' border='0' cellpadding='0' cellspacing='0' style='width: 100%;' width='100%'>
                                                      <tbody>
                                                        <tr>
                                                          <td style='line-height: 40px; font-size: 40px; width: 100%; height: 40px; margin: 0;' align='left' width='100%' height='40'>
                                                            &#160;
                                                          </td>
                                                        </tr>
                                                      </tbody>
                                                    </table>
                                                    <table class='ax-center' role='presentation' align='center' border='0' cellpadding='0' cellspacing='0' style='margin: 0 auto;'>
                                                      <tbody>
                                                        <tr>
                                                          <td style='line-height: 24px; font-size: 16px; margin: 0;' align='left'>
                                                            <img class='w-32' src='https://assets.bootstrapemail.com/logos/dark/combined.png' style='height: auto; line-height: 100%; outline: none; text-decoration: none; display: block; width: 128px; border: 0 none;' width='128'>
                                                          </td>
                                                        </tr>
                                                      </tbody>
                                                    </table>
                                                    <table class='s-10 w-full' role='presentation' border='0' cellpadding='0' cellspacing='0' style='width: 100%;' width='100%'>
                                                      <tbody>
                                                        <tr>
                                                          <td style='line-height: 40px; font-size: 40px; width: 100%; height: 40px; margin: 0;' align='left' width='100%' height='40'>
                                                            &#160;
                                                          </td>
                                                        </tr>
                                                      </tbody>
                                                    </table>
                                                    <table class='ax-center' role='presentation' align='center' border='0' cellpadding='0' cellspacing='0' style='margin: 0 auto;'>
                                                      <tbody>
                                                        <tr>
                                                          <td style='line-height: 24px; font-size: 16px; margin: 0;' align='left'>
                                                            <img class='max-w-56  rounded-lg' src='{imagesecond}' style='height: auto; line-height: 100%; outline: none; text-decoration: none; display: block; border-radius: 8px; max-width: 224px; width: 100%; border: 0 none;' width='224'>
                                                          </td>
                                                        </tr>
                                                      </tbody>
                                                    </table>
                                                    <table class='s-10 w-full' role='presentation' border='0' cellpadding='0' cellspacing='0' style='width: 100%;' width='100%'>
                                                      <tbody>
                                                        <tr>
                                                          <td style='line-height: 40px; font-size: 40px; width: 100%; height: 40px; margin: 0;' align='left' width='100%' height='40'>
                                                            &#160;
                                                          </td>
                                                        </tr>
                                                      </tbody>
                                                    </table>
                                                    <table class='ax-center' role='presentation' align='center' border='0' cellpadding='0' cellspacing='0' style='margin: 0 auto;'>
                                                      <tbody>
                                                        <tr>
                                                          <td style='line-height: 24px; font-size: 16px; margin: 0;' align='left'>
                                                            <p class='max-w-96 lh-lg text-white text-center text-2xl' style='line-height: 2; font-size: 24px; color: #ffffff; max-width: 384px; -premailer-width: 384; width: 100%; margin: 0;' align='center'>
                                                              {textsecond}
                                                            </p>
                                                          </td>
                                                        </tr>
                                                      </tbody>
                                                    </table>
                                                    <table class='s-10 w-full' role='presentation' border='0' cellpadding='0' cellspacing='0' style='width: 100%;' width='100%'>
                                                      <tbody>
                                                        <tr>
                                                          <td style='line-height: 40px; font-size: 40px; width: 100%; height: 40px; margin: 0;' align='left' width='100%' height='40'>
                                                            &#160;
                                                          </td>
                                                        </tr>
                                                      </tbody>
                                                    </table>
                                                    <table class='btn btn-yellow-300 rounded-full fw-800 text-5xl py-4 ax-center  w-full w-lg-80' role='presentation' align='center' border='0' cellpadding='0' cellspacing='0' style='border-radius: 9999px; border-collapse: separate !important; width: 320px; font-size: 48px; line-height: 57.6px; font-weight: 800 !important; margin: 0 auto;' width='320'>
                                                      <tbody>
                                                        <tr>
                                                          <td style='line-height: 24px; font-size: 16px; border-radius: 9999px; width: 320px; font-weight: 800 !important; margin: 0;' align='center' bgcolor='#ffda6a' width='320'>
                                                            <a href='https://bootstrapemail.com' style='color: #111111; font-size: 16px; font-family: Helvetica, Arial, sans-serif; text-decoration: none; border-radius: 9999px; line-height: 20px; display: inline-block; font-weight: 800 !important; white-space: nowrap; background-color: #ffda6a; padding: 16px 12px; border: 1px solid #ffda6a;'>Open</a>
                                                          </td>
                                                        </tr>
                                                      </tbody>
                                                    </table>
                                                    <table class='s-10 w-full' role='presentation' border='0' cellpadding='0' cellspacing='0' style='width: 100%;' width='100%'>
                                                      <tbody>
                                                        <tr>
                                                          <td style='line-height: 40px; font-size: 40px; width: 100%; height: 40px; margin: 0;' align='left' width='100%' height='40'>
                                                            &#160;
                                                          </td>
                                                        </tr>
                                                      </tbody>
                                                    </table>
                                                    <table class='s-6 w-full' role='presentation' border='0' cellpadding='0' cellspacing='0' style='width: 100%;' width='100%'>
                                                      <tbody>
                                                        <tr>
                                                          <td style='line-height: 24px; font-size: 24px; width: 100%; height: 24px; margin: 0;' align='left' width='100%' height='24'>
                                                            &#160;
                                                          </td>
                                                        </tr>
                                                      </tbody>
                                                    </table>
                                                    <div class='text-muted text-center' style='color: #718096;' align='center'>
                                                    </div>
                                                    <table class='s-6 w-full' role='presentation' border='0' cellpadding='0' cellspacing='0' style='width: 100%;' width='100%'>
                                                      <tbody>
                                                        <tr>
                                                          <td style='line-height: 24px; font-size: 24px; width: 100%; height: 24px; margin: 0;' align='left' width='100%' height='24'>
                                                            &#160;
                                                          </td>
                                                        </tr>
                                                      </tbody>
                                                    </table>
                                                    <table class='s-10 w-full' role='presentation' border='0' cellpadding='0' cellspacing='0' style='width: 100%;' width='100%'>
                                                      <tbody>
                                                        <tr>
                                                          <td style='line-height: 40px; font-size: 40px; width: 100%; height: 40px; margin: 0;' align='left' width='100%' height='40'>
                                                            &#160;
                                                          </td>
                                                        </tr>
                                                      </tbody>
                                                    </table>
                                                    <table class='ax-center' role='presentation' align='center' border='0' cellpadding='0' cellspacing='0' style='margin: 0 auto;'>
                                                      <tbody>
                                                        <tr>
                                                          <td style='line-height: 24px; font-size: 16px; margin: 0;' align='left'>
                                                            <img class='w-32' src='https://assets.bootstrapemail.com/logos/dark/combined.png' style='height: auto; line-height: 100%; outline: none; text-decoration: none; display: block; width: 128px; border: 0 none;' width='128'>
                                                          </td>
                                                        </tr>
                                                      </tbody>
                                                    </table>
                                                    <table class='s-10 w-full' role='presentation' border='0' cellpadding='0' cellspacing='0' style='width: 100%;' width='100%'>
                                                      <tbody>
                                                        <tr>
                                                          <td style='line-height: 40px; font-size: 40px; width: 100%; height: 40px; margin: 0;' align='left' width='100%' height='40'>
                                                            &#160;
                                                          </td>
                                                        </tr>
                                                      </tbody>
                                                    </table>
                                                    <table class='ax-center' role='presentation' align='center' border='0' cellpadding='0' cellspacing='0' style='margin: 0 auto;'>
                                                      <tbody>
                                                        <tr>
                                                          <td style='line-height: 24px; font-size: 16px; margin: 0;' align='left'>
                                                            <img class='max-w-56  rounded-lg' src='{imagethird}' style='height: auto; line-height: 100%; outline: none; text-decoration: none; display: block; border-radius: 8px; max-width: 224px; width: 100%; border: 0 none;' width='224'>
                                                          </td>
                                                        </tr>
                                                      </tbody>
                                                    </table>
                                                    <table class='s-10 w-full' role='presentation' border='0' cellpadding='0' cellspacing='0' style='width: 100%;' width='100%'>
                                                      <tbody>
                                                        <tr>
                                                          <td style='line-height: 40px; font-size: 40px; width: 100%; height: 40px; margin: 0;' align='left' width='100%' height='40'>
                                                            &#160;
                                                          </td>
                                                        </tr>
                                                      </tbody>
                                                    </table>
                                                    <table class='ax-center' role='presentation' align='center' border='0' cellpadding='0' cellspacing='0' style='margin: 0 auto;'>
                                                      <tbody>
                                                        <tr>
                                                          <td style='line-height: 24px; font-size: 16px; margin: 0;' align='left'>
                                                            <p class='max-w-96 lh-lg text-white text-center text-2xl' style='line-height: 2; font-size: 24px; color: #ffffff; max-width: 384px; -premailer-width: 384; width: 100%; margin: 0;' align='center'>
                                                              {textthird}
                                                            </p>
                                                          </td>
                                                        </tr>
                                                      </tbody>
                                                    </table>
                                                    <table class='s-10 w-full' role='presentation' border='0' cellpadding='0' cellspacing='0' style='width: 100%;' width='100%'>
                                                      <tbody>
                                                        <tr>
                                                          <td style='line-height: 40px; font-size: 40px; width: 100%; height: 40px; margin: 0;' align='left' width='100%' height='40'>
                                                            &#160;
                                                          </td>
                                                        </tr>
                                                      </tbody>
                                                    </table>
                                                    <table class='btn btn-yellow-300 rounded-full fw-800 text-5xl py-4 ax-center  w-full w-lg-80' role='presentation' align='center' border='0' cellpadding='0' cellspacing='0' style='border-radius: 9999px; border-collapse: separate !important; width: 320px; font-size: 48px; line-height: 57.6px; font-weight: 800 !important; margin: 0 auto;' width='320'>
                                                      <tbody>
                                                        <tr>
                                                          <td style='line-height: 24px; font-size: 16px; border-radius: 9999px; width: 320px; font-weight: 800 !important; margin: 0;' align='center' bgcolor='#ffda6a' width='320'>
                                                            <a href='https://bootstrapemail.com' style='color: #111111; font-size: 16px; font-family: Helvetica, Arial, sans-serif; text-decoration: none; border-radius: 9999px; line-height: 20px; display: inline-block; font-weight: 800 !important; white-space: nowrap; background-color: #ffda6a; padding: 16px 12px; border: 1px solid #ffda6a;'>Open</a>
                                                          </td>
                                                        </tr>
                                                      </tbody>
                                                    </table>
                                                    <table class='s-10 w-full' role='presentation' border='0' cellpadding='0' cellspacing='0' style='width: 100%;' width='100%'>
                                                      <tbody>
                                                        <tr>
                                                          <td style='line-height: 40px; font-size: 40px; width: 100%; height: 40px; margin: 0;' align='left' width='100%' height='40'>
                                                            &#160;
                                                          </td>
                                                        </tr>
                                                      </tbody>
                                                    </table>
                                                    <table class='s-6 w-full' role='presentation' border='0' cellpadding='0' cellspacing='0' style='width: 100%;' width='100%'>
                                                      <tbody>
                                                        <tr>
                                                          <td style='line-height: 24px; font-size: 24px; width: 100%; height: 24px; margin: 0;' align='left' width='100%' height='24'>
                                                            &#160;
                                                          </td>
                                                        </tr>
                                                      </tbody>
                                                    </table>
                                                    <div class='text-muted text-center' style='color: #718096;' align='center'>
                                                    </div>
                                                    <table class='s-6 w-full' role='presentation' border='0' cellpadding='0' cellspacing='0' style='width: 100%;' width='100%'>
                                                      <tbody>
                                                        <tr>
                                                          <td style='line-height: 24px; font-size: 24px; width: 100%; height: 24px; margin: 0;' align='left' width='100%' height='24'>
                                                            &#160;
                                                          </td>
                                                        </tr>
                                                      </tbody>
                                                    </table>
                                                    <table class='s-10 w-full' role='presentation' border='0' cellpadding='0' cellspacing='0' style='width: 100%;' width='100%'>
                                                      <tbody>
                                                        <tr>
                                                          <td style='line-height: 40px; font-size: 40px; width: 100%; height: 40px; margin: 0;' align='left' width='100%' height='40'>
                                                            &#160;
                                                          </td>
                                                        </tr>
                                                      </tbody>
                                                    </table>
                                                    <table class='ax-center' role='presentation' align='center' border='0' cellpadding='0' cellspacing='0' style='margin: 0 auto;'>
                                                      <tbody>
                                                        <tr>
                                                          <td style='line-height: 24px; font-size: 16px; margin: 0;' align='left'>
                                                            <img class='w-32' src='https://assets.bootstrapemail.com/logos/dark/combined.png' style='height: auto; line-height: 100%; outline: none; text-decoration: none; display: block; width: 128px; border: 0 none;' width='128'>
                                                          </td>
                                                        </tr>
                                                      </tbody>
                                                    </table>
                                                    <table class='s-10 w-full' role='presentation' border='0' cellpadding='0' cellspacing='0' style='width: 100%;' width='100%'>
                                                      <tbody>
                                                        <tr>
                                                          <td style='line-height: 40px; font-size: 40px; width: 100%; height: 40px; margin: 0;' align='left' width='100%' height='40'>
                                                            &#160;
                                                          </td>
                                                        </tr>
                                                      </tbody>
                                                    </table>
                                                    <table class='ax-center' role='presentation' align='center' border='0' cellpadding='0' cellspacing='0' style='margin: 0 auto;'>
                                                      <tbody>
                                                        <tr>
                                                          <td style='line-height: 24px; font-size: 16px; margin: 0;' align='left'>
                                                            <img class='max-w-56  rounded-lg' src='{imageforth}' style='height: auto; line-height: 100%; outline: none; text-decoration: none; display: block; border-radius: 8px; max-width: 224px; width: 100%; border: 0 none;' width='224'>
                                                          </td>
                                                        </tr>
                                                      </tbody>
                                                    </table>
                                                    <table class='s-10 w-full' role='presentation' border='0' cellpadding='0' cellspacing='0' style='width: 100%;' width='100%'>
                                                      <tbody>
                                                        <tr>
                                                          <td style='line-height: 40px; font-size: 40px; width: 100%; height: 40px; margin: 0;' align='left' width='100%' height='40'>
                                                            &#160;
                                                          </td>
                                                        </tr>
                                                      </tbody>
                                                    </table>
                                                    <table class='ax-center' role='presentation' align='center' border='0' cellpadding='0' cellspacing='0' style='margin: 0 auto;'>
                                                      <tbody>
                                                        <tr>
                                                          <td style='line-height: 24px; font-size: 16px; margin: 0;' align='left'>
                                                            <p class='max-w-96 lh-lg text-white text-center text-2xl' style='line-height: 2; font-size: 24px; color: #ffffff; max-width: 384px; -premailer-width: 384; width: 100%; margin: 0;' align='center'>
                                                              {textforth}
                                                            </p>
                                                          </td>
                                                        </tr>
                                                      </tbody>
                                                    </table>
                                                    <table class='s-10 w-full' role='presentation' border='0' cellpadding='0' cellspacing='0' style='width: 100%;' width='100%'>
                                                      <tbody>
                                                        <tr>
                                                          <td style='line-height: 40px; font-size: 40px; width: 100%; height: 40px; margin: 0;' align='left' width='100%' height='40'>
                                                            &#160;
                                                          </td>
                                                        </tr>
                                                      </tbody>
                                                    </table>
                                                    <table class='btn btn-yellow-300 rounded-full fw-800 text-5xl py-4 ax-center  w-full w-lg-80' role='presentation' align='center' border='0' cellpadding='0' cellspacing='0' style='border-radius: 9999px; border-collapse: separate !important; width: 320px; font-size: 48px; line-height: 57.6px; font-weight: 800 !important; margin: 0 auto;' width='320'>
                                                      <tbody>
                                                        <tr>
                                                          <td style='line-height: 24px; font-size: 16px; border-radius: 9999px; width: 320px; font-weight: 800 !important; margin: 0;' align='center' bgcolor='#ffda6a' width='320'>
                                                            <a href='https://bootstrapemail.com' style='color: #111111; font-size: 16px; font-family: Helvetica, Arial, sans-serif; text-decoration: none; border-radius: 9999px; line-height: 20px; display: inline-block; font-weight: 800 !important; white-space: nowrap; background-color: #ffda6a; padding: 16px 12px; border: 1px solid #ffda6a;'>Open</a>
                                                          </td>
                                                        </tr>
                                                      </tbody>
                                                    </table>
                                                    <table class='s-10 w-full' role='presentation' border='0' cellpadding='0' cellspacing='0' style='width: 100%;' width='100%'>
                                                      <tbody>
                                                        <tr>
                                                          <td style='line-height: 40px; font-size: 40px; width: 100%; height: 40px; margin: 0;' align='left' width='100%' height='40'>
                                                            &#160;
                                                          </td>
                                                        </tr>
                                                      </tbody>
                                                    </table>
                                                    <table class='s-6 w-full' role='presentation' border='0' cellpadding='0' cellspacing='0' style='width: 100%;' width='100%'>
                                                      <tbody>
                                                        <tr>
                                                          <td style='line-height: 24px; font-size: 24px; width: 100%; height: 24px; margin: 0;' align='left' width='100%' height='24'>
                                                            &#160;
                                                          </td>
                                                        </tr>
                                                      </tbody>
                                                    </table>
                                                    <div class='text-muted text-center' style='color: #718096;' align='center'>
                                                    </div>
                                                    <table class='s-6 w-full' role='presentation' border='0' cellpadding='0' cellspacing='0' style='width: 100%;' width='100%'>
                                                      <tbody>
                                                        <tr>
                                                          <td style='line-height: 24px; font-size: 24px; width: 100%; height: 24px; margin: 0;' align='left' width='100%' height='24'>
                                                            &#160;
                                                          </td>
                                                        </tr>
                                                      </tbody>
                                                    </table>
                                                  </td>
                                                </tr>
                                              </tbody>
                                            </table>
                                            <!--[if (gte mso 9)|(IE)]>
                                          </td>
                                        </tr>
                                      </tbody>
                                    </table>
                                    <![endif]-->
                                  </td>
                                </tr>
                              </tbody>
                            </table>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </td>
                </tr>
              </tbody>
            </table>
          </body>
        </html>
        """


    # Turn these into plain/html MIMEText objects
    part2 = MIMEText(html, 'html')
    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
