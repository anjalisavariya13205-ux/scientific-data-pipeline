from kafka import KafkaConsumer
import json
import pandas as pd
from datetime import datetime
from collections import defaultdict
import time
import os

# Create output directory
if not os.path.exists('output'):
    os.makedirs('output')

consumer = KafkaConsumer(
    'particle-events',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='latest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("🚀 Advanced Particle Event Analytics Started")
print("=" * 70)

# Storage for analytics
all_events = []
high_energy_events = []
anomalies = []
particle_counts = defaultdict(int)
detector_counts = defaultdict(int)
energy_by_particle = defaultdict(list)

event_count = 0
start_time = time.time()

try:
    for message in consumer:
        event = message.value
        event_count += 1
        
        # Store event
        all_events.append(event)
        
        # Track particle types
        particle_counts[event['particle_type']] += 1
        
        # Track detectors
        detector_counts[event['detector_id']] += 1
        
        # Track energy by particle
        energy_by_particle[event['particle_type']].append(event['energy_gev'])
        
        # Filter high energy events
        if event['energy_gev'] > 100:
            high_energy_events.append(event)
        
        # Track anomalies
        if event['is_anomaly']:
            anomalies.append(event)
            print(f"🚨 ANOMALY DETECTED!")
            print(f"   Event ID: {event['event_id']}")
            print(f"   Particle: {event['particle_type']}, Energy: {event['energy_gev']} GeV")
            print("-" * 70)
        
        # Every 50 events, show statistics
        if event_count % 50 == 0:
            elapsed = time.time() - start_time
            events_per_sec = event_count / elapsed
            
            print(f"\n📊 STATISTICS (after {event_count} events)")
            print(f"   Time elapsed: {elapsed:.1f}s | Rate: {events_per_sec:.1f} events/sec")
            print(f"\n   Particle Distribution:")
            for particle, count in particle_counts.items():
                avg_energy = sum(energy_by_particle[particle]) / len(energy_by_particle[particle])
                print(f"     {particle:10s}: {count:4d} events | Avg Energy: {avg_energy:6.2f} GeV")
            
            print(f"\n   Detector Activity:")
            for detector, count in detector_counts.items():
                print(f"     {detector}: {count} events")
            
            print(f"\n   High Energy Events (>100 GeV): {len(high_energy_events)}")
            print(f"   Anomalies Detected: {len(anomalies)}")
            print("=" * 70)
        
        # Every 100 events, save to files
        if event_count % 100 == 0:
            # Save high energy events
            if high_energy_events:
                df_high = pd.DataFrame(high_energy_events)
                filename = f"output/high_energy_events_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
                df_high.to_csv(filename, index=False)
                print(f"💾 Saved {len(high_energy_events)} high-energy events to {filename}")
            
            # Save anomalies
            if anomalies:
                df_anomalies = pd.DataFrame(anomalies)
                filename = f"output/anomalies_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
                df_anomalies.to_csv(filename, index=False)
                print(f"💾 Saved {len(anomalies)} anomalies to {filename}")
            
            # Save statistics summary
            stats = {
                'total_events': event_count,
                'high_energy_count': len(high_energy_events),
                'anomaly_count': len(anomalies),
                'particle_distribution': dict(particle_counts),
                'detector_distribution': dict(detector_counts)
            }
            
            with open(f"output/statistics_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json", 'w') as f:
                json.dump(stats, f, indent=2)
            
            print(f"💾 Saved statistics summary")
            print("=" * 70)

except KeyboardInterrupt:
    print(f"\n\n🛑 Analytics Stopped")
    print(f"\n📈 FINAL SUMMARY:")
    print(f"   Total Events Processed: {event_count}")
    print(f"   High Energy Events: {len(high_energy_events)} ({len(high_energy_events)/event_count*100:.1f}%)")
    print(f"   Anomalies Found: {len(anomalies)} ({len(anomalies)/event_count*100:.1f}%)")
    print(f"\n   Final Particle Distribution:")
    for particle, count in particle_counts.items():
        print(f"     {particle}: {count} ({count/event_count*100:.1f}%)")
    
    # Save final datasets
    if all_events:
        df_all = pd.DataFrame(all_events)
        df_all.to_csv('output/all_events_final.csv', index=False)
        print(f"\n💾 Final dataset saved to output/all_events_final.csv")
    
    consumer.close()