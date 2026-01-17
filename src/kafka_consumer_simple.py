from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'particle-events',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='latest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("Listening for particle events...")
print("=" * 60)

try:
    for message in consumer:
        event = message.value
        if event['energy_gev'] > 100:
            print(f"High Energy Event Detected!")
            print(f"  Event ID: {event['event_id']}")
            print(f"  Particle: {event['particle_type']}")
            print(f"  Energy: {event['energy_gev']} GeV")
            print(f"  Detector: {event['detector_id']}")
            print(f"  Anomaly: {event['is_anomaly']}")
            print("-" * 60)
except KeyboardInterrupt:
    print("\nStopped consumer")
    consumer.close()