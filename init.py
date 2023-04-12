from influxdb_client import InfluxDBClient
import datetime
from influxdb_client.client.write_api import SYNCHRONOUS

influxdb_url = "http://localhost:8086"
influxdb_token = "LdNKSCdKd6-ogUkzK51D8TDTE88X2rvsTwKG3uOuiFoLJSrPJkg424UfWV9G52eoNz47OYW4YSCnEWwgI9a2rw=="  # InfluxDB에서 생성한 토큰
influxdb_org = " kangwon_univercity"  # InfluxDB의 조직 이름
influxdb_bucket = "capstone"  # InfluxDB에서 생성한 버킷 이름


client = InfluxDBClient(url=influxdb_url, token=influxdb_token)

# 공공데이터 수집 (예시)
data_points = [
    {'timestamp': '2023-04-12T00:00:00Z', 'location': 'Seoul', 'temperature': 15.0},
    {'timestamp': '2023-04-12T01:00:00Z', 'location': 'Seoul', 'temperature': 14.5},
]

# 시계열 데이터로 변환
time_series_data = []
for data in data_points:
    point = {
        "measurement": "temperature",
        "tags": {
            "location": data['location'],
        },
        "fields": {
            "value": data['temperature'],
        },
        "time": data['timestamp'],
    }
    time_series_data.append(point)



write_api = client.write_api(write_options=SYNCHRONOUS)

write_api.write(bucket=influxdb_bucket, org=influxdb_org, record=time_series_data)

# 클라이언트 종료
client.close()