from kafka import KafkaProducer
from csv import reader

def kafka_python_producer_sync(producer, msg, topic):
    producer.send(topic, bytes(msg, encoding='utf-8'))
    print("Sending " + msg)
    producer.flush(timeout=60)


def success(metadata):
    print(metadata.topic)


def error(exception):
    print(exception)


def kafka_python_producer_async(producer, msg, topic):
    producer.send(topic, bytes(msg, encoding='utf-8')).add_callback(success).add_errback(error)
    producer.flush()


if __name__ == '__main__':
    producer = KafkaProducer(bootstrap_servers='35.226.9.245:9092')  # use your VM's external IP Here!
    with open("C:\Software_JADS\DEAssignment2\lab7\data\game\DEassignment2_data\stream_2008_till_8_2e.csv", "r") as f:
        rows = f.readlines()
        #csv_reader = reader(f)
        #header = next(csv_reader)
        #if header != None:
        #    for row in csv_reader:
        #        kafka_python_producer_sync(producer, row, 'input_stream')

    for row in rows:
        kafka_python_producer_sync(producer, row, 'input_stream')

        
    f.close()
