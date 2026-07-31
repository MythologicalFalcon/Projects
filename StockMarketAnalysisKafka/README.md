# StockMarketAnalysisKafka

Streams stock index data through Kafka into S3, then makes it queryable with Glue and
Athena. The Kafka broker runs on an EC2 instance rather than a managed service, so this
covers the setup as well as the code.

`Architecture.jpg` shows the flow.

## How it works

`kafkaProducer.py` reads `indexProcessed.csv` and publishes rows to the `demo_test` topic
on a loop, so a static CSV behaves like a live feed.

`kafkaConsumer.py` subscribes to the same topic and writes each message to
`s3://<your-bucket>/stock_market_<n>.json` through `s3fs`. Empty messages are skipped and
logged rather than written.

From there a Glue Crawler catalogues the JSON sitting in S3, and Athena queries it as SQL.

## Setup

`commands.txt` has the full EC2 and Kafka install as it was run. The outline:

1. Launch an EC2 instance and open port 9092 to your IP in the security group.
2. Install Java, then download and extract Kafka 3.3.1.
3. Start ZooKeeper, then the broker, with `advertised.listeners` set to the instance
   public IP. Leave it as localhost and remote clients resolve the wrong address.
4. Create the `demo_test` topic.
5. Give the instance an IAM role with write access to your S3 bucket.

Both scripts carry `{Instance public IP}` as a placeholder for the broker address, and the
consumer has a hardcoded bucket name. Replace both before running.

```
pip install -r requirements.txt
python kafkaProducer.py   # one terminal
python kafkaConsumer.py   # another
```

## Scope

Around 100 lines of Python. The value is the pipeline and the AWS setup around it rather
than the code. There is no schema validation, no consumer group or offset management, and
no retry on a failed S3 write.

## Stack

Python, Apache Kafka, kafka-python, pandas, s3fs, AWS EC2, S3, Glue Crawler, Athena, IAM.
