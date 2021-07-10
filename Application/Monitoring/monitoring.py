from kafka import KafkaConsumer

temperature_consumer = KafkaConsumer('temperature', bootstrap_servers=['127.0.0.1:9092'])
electrical_consumer = KafkaConsumer('electrical', bootstrap_servers=['127.0.0.1:9092'])
oxygen_consumer = KafkaConsumer('oxygen', bootstrap_servers=['127.0.0.1:9092'])
fire_consumer = KafkaConsumer('fire', bootstrap_servers=['127.0.0.1:9092'])
