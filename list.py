import json
import boto3
EC2 = boto3.client('ec2')
DYNAMODB = boto3.client('dynamodb')

def main():
    res_regions = EC2.describe_regions()
    regions = res_regions['Regions']
    for r in regions:
        print(json.dumps(r['RegionName']))
    res_tables = DYNAMODB.list_tables()

    print(json.dumps(res_tables))


if __name__ == "__main__":
    main()
