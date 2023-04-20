cd /code/lightgbm
LOG_OUT=./stdout.log
LOG_ERR=./stderr.log

exec 1>>$LOG_OUT
exec 2>>$LOG_ERR

echo start

docker exec -d lightgbm-web-1 python /app/model/processing.py $1 $2

# docker run --rm -v /home/ubuntu/ec2_web/app:/app -w /app --name $2 lightgbm-web
# python /app/model/processing.py $1 $2
# exit