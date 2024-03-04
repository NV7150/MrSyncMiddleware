# Augma Protocol
ver. 0.1 Alpha <br>
Author: dang0

## What's this?
This protocol is Pub/Sub based real-time socket communication protocol
that used to communicate real field (assumed MR/AR) and virtual
space (assumed VR or Digital Twin concept).<br>

## Specifics
### Pub/Sub based data translation
- Each data will be delivered only if you subscribe it
- The subscribe data is pushed as soon as when it is published

### Return subscribing


## Base Protocol

### Publish
#### Request
```json lines
{
  "topic": str,
  "content": {
    // some contents you want to publish
  }
}
```

#### Response
```json lines
N/A // maybe implement result response someday
```

### Subscribe
Subscribe means request server to call back every time if the topic is
published until unsubscribed.
#### Request
```json
{
  "topic": "subscribe",
  "content": {
    "topic": "topic you want to subscribe"
  }
}
```
#### Response
```json lines
N/A // maybe implement result response someday
```
#### Subscribe Response
```json lines
{
  "topic": str,
  "idx":  "client id of publisher",
  "content": {
    // some contents that published by publisher
  }
}
```

### Unsubscribe
#### Request
```json
{
  "topic": "unsubscribe",
  "content": {
    "topic": "topic you want to unsubscribe"
  }
}
```
#### Response
```json lines
N/A // maybe implement result response someday
```

### Pull
Pull means directory pull the latest content.
#### Request
```json
{
  "topic": "pull",
  "content": {
    "topic": "topic you want to pull"
  }
}
```
#### Response
```json lines
{
  "topic": str,
  "idx": "client id of publisher",
  "content": {
    // some contents that published by publisher
  }
}
```



## Update History
- 2023-10-30 ver. Alpha 0.1 Created alpha document
