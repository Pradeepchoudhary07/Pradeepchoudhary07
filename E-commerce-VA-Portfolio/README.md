# E-commerce VA Portfolio

This folder contains example automations and a small Python demo that simulates processing orders for an online store.

What's included

- demo-order-assistant/: a small Python script that reads an orders CSV and marks orders as processed.
- sample workflows: order intake, fulfillment messaging, and returns handling outlines.

Sample workflow (Order processing)

1. New order arrives via CSV or webhook.
2. Validate order fields and payment status.
3. Create fulfillment task and update inventory.
4. Send customer confirmation message with tracking placeholder.

Files

- demo-order-assistant/app.py — demo script
- demo-order-assistant/orders.csv — sample orders
- demo-order-assistant/README.md — how to run the demo
