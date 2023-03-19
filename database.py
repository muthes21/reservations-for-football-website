from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://pd1ingcxwezsxx33lheb:pscale_pw_qJAUsqSsHYsshWlEQ90c0MFr0tMPYWY669bQflIll6V@apsouth.connect.psdb.cloud/reservationsforfootball?charset=utf8mb4"


engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl":{
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })

with engine.connect() as conn:
  result = conn.execute(text("SELECT * FROM reservationsforfootball"))
  print(result.all())