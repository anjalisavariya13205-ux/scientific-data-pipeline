import json
import random
import time
from datetime import datetime
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_particle_event():
    event = {
        'event_id': random.randint(1000000, 9999999),
        'timestamp': datetime.utcnow().isoformat(),
        'particle_type': random.choice(['electron', 'muon', 'photon', 'proton']),
        'energy_gev': round(random.uniform(0.5, 1000.0), 2),
        'momentum_x': round(random.uniform(-500, 500), 2),
        'momentum_y': round(random.uniform(-500, 500), 2),
        'momentum_z': round(random.uniform(-500, 500), 2),
        'detector_id': random.choice(['DET_001', 'DET_002', 'DET_003']),
        'is_anomaly': random.random() < 0.05
    }
    return event

print("Starting particle event generator...")

try:
    event_count = 0
    while True:
        event = generate_particle_event()
        producer.send('particle-events', value=event)
        event_count += 1
        
        if event_count % 10 == 0:
            print(f"Sent {event_count} events")
        
        time.sleep(0.1)

except KeyboardInterrupt:
    print(f"\nStopped. Total events sent: {event_count}")
    producer.close()