#!/usr/bin/env python3
"""Simple order processing demo.

Reads orders.csv and writes processed_orders.csv with a status column.
"""
import csv

INPUT = 'E-commerce-VA-Portfolio/demo-order-assistant/orders.csv'
OUTPUT = 'E-commerce-VA-Portfolio/demo-order-assistant/processed_orders.csv'

def process_order(row):
    # Minimal validation and processing logic
    status = 'processed' if row.get('order_id') else 'error'
    tracking = f'TRK{row.get("order_id")}' if status == 'processed' else ''
    return {**row, 'status': status, 'tracking_number': tracking}

def main():
    with open(INPUT, newline='') as fin:
        reader = csv.DictReader(fin)
        processed = [process_order(r) for r in reader]

    fieldnames = list(processed[0].keys()) if processed else []
    with open(OUTPUT, 'w', newline='') as fout:
        writer = csv.DictWriter(fout, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(processed)

    print(f'Wrote {len(processed)} processed orders to {OUTPUT}')

if __name__ == '__main__':
    main()
