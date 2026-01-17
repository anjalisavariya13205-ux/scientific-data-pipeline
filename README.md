# Scalable Real-Time Scientific Data Pipeline

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Kafka](https://img.shields.io/badge/Apache%20Kafka-3.6-orange.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

A real-time streaming data pipeline that simulates scientific event processing using Apache Kafka and Python.  
This project demonstrates core data engineering concepts such as event streaming, real-time analytics, fault tolerance, and structured data storage.

## 📌 Project Summary

This project implements an end-to-end real-time data pipeline that:

- **Generates** synthetic scientific event data  
- **Streams** events through Apache Kafka  
- **Processes** data in real time using Python consumers  
- **Applies** filtering and anomaly detection logic  
- **Stores** structured outputs for downstream analysis  

The focus of this project is **architecture, data flow, and engineering practices**, not domain-specific claims.

## 🏗️ System Architecture
```
┌─────────────────────┐      ┌──────────────────┐      ┌─────────────────────┐
│  Data Generator     │─────▶│   Apache Kafka   │─────▶│  Analytics Engine   │
│  (Python Producer)  │      │  (Message Queue) │      │  (Python Consumer)  │
└─────────────────────┘      └──────────────────┘      └─────────────────────┘
       Event creation           Fault-tolerant              Real-time filtering
       & serialization          event streaming             & analytics
                                                                    │
                                                                    ▼
                                                            ┌─────────────────┐
                                                            │  Output Files   │
                                                            │   (CSV / JSON)  │
                                                            └─────────────────┘
```

## ✨ Key Features

- ✅ **Real-time event streaming** using Kafka
- ✅ **Producer–consumer architecture**
- ✅ **Fault-tolerant message handling**
- ✅ **Event filtering** based on configurable thresholds
- ✅ **Anomaly flagging** for rare events
- ✅ **Periodic aggregation** and statistics reporting
- ✅ **Automatic persistence** of processed data

## 📊 Event Data Schema

Each event follows a structured format:
```json
{
  "event_id": 123456,
  "timestamp": "2026-01-16T10:23:45.123456",
  "particle_type": "muon",
  "energy_gev": 234.56,
  "momentum_x": 123.45,
  "momentum_y": -67.89,
  "momentum_z": 345.67,
  "detector_id": "DET_001",
  "is_anomaly": false
}
```

## 📁 Project Structure
```
Kafka_Spark_Pipeline/
│
├── data/
│   └── all_events_final.csv
│
├── src/
│   ├── data_generator.py
│   ├── kafka_consumer_simple.py
│   └── kafka_consumer_advanced.py
│
├── notebooks/
│   └── data_overview.ipynb
│
├── results/
│   ├── high_energy_events_*.csv
│   ├── anomalies_*.csv
│   └── statistics_*.json
│
├── README.md
├── requirements.txt
└── .gitignore
```

## 🚀 Setup & Execution

### Prerequisites

- Python 3.8+
- Java 11+
- Apache Kafka 3.6+

### Install Dependencies
```bash
pip install kafka-python pandas
```

### Start Kafka Services

**Zookeeper:**
```bash
bin\windows\zookeeper-server-start.bat config\zookeeper.properties
```

**Kafka Broker:**
```bash
bin\windows\kafka-server-start.bat config\server.properties
```

### Create Topic
```bash
bin\windows\kafka-topics.bat --create --topic particle-events --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```

### Run the Pipeline

**Start Data Generator:**
```bash
python src/data_generator.py
```

**Start Analytics Consumer:**
```bash
python src/kafka_consumer_advanced.py
```

## 📈 Output

The pipeline generates:

- **Final combined dataset** (`all_events_final.csv`)
- **Filtered high-energy events**
- **Anomaly records**
- **Periodic statistics summaries**

A Jupyter notebook is included to quickly inspect and validate results.

## 🎯 Learning Outcomes

This project demonstrates:

- Event-driven system design
- Real-time data ingestion pipelines
- Kafka-based messaging patterns
- Python-based stream analytics
- Data validation and persistence
- Clean project structuring for GitHub portfolios

## 🔮 Future Improvements

- [ ] Spark-based distributed processing
- [ ] Machine learning–based anomaly detection
- [ ] Real-time dashboards
- [ ] Dockerized deployment
- [ ] Multi-broker Kafka setup

## 👤 Author

**Anjali Savariya**  
BCA (Big Data Analytics) Student | Aspiring Data Engineer

[![GitHub](https://img.shields.io/badge/GitHub-anjalisavariya13205--ux-181717?logo=github)](https://github.com/anjalisavariya13205-ux)

## 📄 License

MIT License — free to use for learning and experimentation.

⭐ **If this project helped you learn, please star this repository!**
