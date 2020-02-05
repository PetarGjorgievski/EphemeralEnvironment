import requests
import boto3

def get_ip():
     client = boto3.client('ec2', region_name='us-east-2')
     result = client.describe_instances()
     IpAddr = (result['Reservations'][0]['Instances'][0]['PublicIpAddress'])
     return IpAddr




def test_server(url):
     r = requests.get(url)
     assert r.status_code == 200, "Status code is not 200!"


test_server('http://'+get_ip())
