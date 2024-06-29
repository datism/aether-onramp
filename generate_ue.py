import json


def generate_config(num_ue, start_imsi, device_group_id):
    # Base configuration template
    config = {
        "default-target": "the-enterprise",
        "Updates": {
            "site-2.1.0": [
                {
                    "description": "Aether Test Site",
                    "display-name": "Aether Site",
                    "site-id": "site-1",
                    "sim-card": [],
                    "device": [],
                    "device-group": [
                        {
                            "display-name": f"Aether Users {device_group_id}",
                            "device-group-id": f"device-group-{device_group_id}",
                            "device": [],
                            "ip-domain": f"ip-pool-{device_group_id}",
                            "traffic-class": f"class-{device_group_id}"                   
                        }
                    ]
                }
            ]
        },
        "Deletes": {},
        "Extensions": {
            "transaction-strategy-111": 1
        }
    }

    # Generate devices and sim-cards
    for i in range(num_ue):
        imsi = start_imsi + i
        ue_id = f"ue-{imsi}"
        sim_id = f"sim1-{imsi}"
        
        # Add device
        config["Updates"]["site-2.1.0"][0]["device"].append({
            "device-id": ue_id,
            "display-name": f"UE {imsi}",
            "sim-card": sim_id
        })
        
        # Add sim-card
        config["Updates"]["site-2.1.0"][0]["sim-card"].append({
            "sim-id": sim_id,
            "display-name": f"SIM {imsi}",
            "imsi": f"208930{imsi:07d}"
        })
        
        # Add device to device-group
        config["Updates"]["site-2.1.0"][0]["device-group"][0]["device"].append({
            "device-id": ue_id,
            "enable": True
        })

    return config

def main():
    # Input: Number of UEs, starting IMSI, and device group ID
    num_ue = int(input("Enter the number of UEs: "))
    start_imsi = int(input("Enter the starting IMSI: "))
    device_group_id = int(input("Enter the device group ID: "))

    # Generate the configuration
    config = generate_config(num_ue, start_imsi, device_group_id)

    # Write the configuration to a JSON file
    with open('config.json', 'w') as f:
        json.dump(config, f, indent=4)

    print("Configuration file 'config.json' generated successfully.")

if __name__ == "__main__":
    main()
