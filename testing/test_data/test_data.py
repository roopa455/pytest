class json_data():

    headers = {
              "Content-Type": "application/json"
    }

    def register_network(self, description, id, name):
        register_network_payload = {
        "description": description,
        "dns": {
            "dhcp_server_enabled": True,
            "enable_caching": False,
            "local_ttl": 0,
            "records": [
            {
                "a_record": [
                "192.88.99.142"
                ],
                "aaaa_record": [
                "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
                ],
                "cname_record": [
                "cname.example.com"
                ],
                "domain": "example.com"
            }
            ]
        },
        "features": {
            "features": {
            "featureName1": "featureProp1",
            "featureName2": "featureProp2"
            }
        },
        "id": id,
        "name": name,
        "sentry_config": {
            "exclusion_patterns": [],
            "number_of_lines_in_log": 0,
            "sample_rate": 1,
            "upload_mme_log": False
        },
        "state_config": {
            "sync_interval": 60
        },
        "type": "LTE"
        }
  
        return register_network_payload

#https://172.16.5.107:9443/magma/v1/networks -get network
#https://172.16.5.107:9443/magma/v1/networks - Post network
#https://172.16.5.107:9443/magma/v1/networks/lte/gateways - get gateway
#https://172.16.5.107:9443/magma/v1/networks/lte/gateways - post gateway

    def add_new_gateway(self, description, hardware_id, key, id):
        gateway_data = {
    "description": description,
    "device": {
        "hardware_id": hardware_id,
        "key": {        
        "key":key,
        "key_type": "SOFTWARE_ECDSA_SHA256"
        }
    },
    "id": id,
    "magmad": {
        "autoupgrade_enabled": True,
        "autoupgrade_poll_interval": 300,
        "checkin_interval": 60,
        "checkin_timeout": 10,
        "dynamic_services": [],
        "feature_flags": {
        "newfeature1": True,
        "newfeature2": false
        },
        "logging": {
        "aggregation": {
            "target_files_by_tag": {
            "enodebd": "/var/log/enodebd.log",
            "mme": "/var/log/mme.log",
            "otherlog": "/var/log/otherlog.log"
            },
            "throttle_interval": "1m",
            "throttle_rate": 1000,
            "throttle_window": 5
        },
        "event_verbosity": 0,
        "log_level": "DEBUG"
        },
        "vpn": {
        "enable_shell": false
        }
    },
    "name": "Sample Gateway",
    "registration_info": {
        "domain_name": "example.com",
        "registration_token": "reg_a9vnap30fN0anrfjVneB",
        "root_ca": "=example rootCA.pem="
    },
    "status": {
        "cert_expiration_time": 1234567890,
        "checkin_time": 1234567890,
        "hardware_id": "string",
        "kernel_version": "4.9.0-6-amd64",
        "kernel_versions_installed": [
        "4.9.0-6-amd64",
        "4.9.0-7-amd64"
        ],
        "machine_info": {
        "cpu_info": {
            "architecture": "x86_64",
            "core_count": 4,
            "model_name": "Intel(R) Core(TM) i9-8950HK CPU @ 2.90GHz",
            "threads_per_core": 1
        },
        "network_info": {
            "network_interfaces": [
            {
                "ip_addresses": [
                "10.10.10.1",
                "10.0.0.1"
                ],
                "ipv6_addresses": [
                "fe80::a00:27ff:fe1e:8332",
                "fe80::a00:27ff:fe1e:8432"
                ],
                "mac_address": "08:00:27:1e:8a:32",
                "network_interface_id": "gtp_br0",
                "status": "UP"
            }
            ],
            "routing_table": [
            {
                "destination_ip": "0.0.0.0",
                "gateway_ip": "10.10.10.1",
                "genmask": "255.255.255.0",
                "network_interface_id": "gtp_br0"
            }
            ]
        }
        },
        "meta": {
        "additionalProp1": "string",
        "additionalProp2": "string",
        "additionalProp3": "string"
        },
        "platform_info": {
        "config_info": {
            "mconfig_created_at": 1552968732
        },
        "kernel_version": "4.9.0-6-amd64",
        "kernel_versions_installed": [
            "4.9.0-6-amd64",
            "4.9.0-7-amd64"
        ],
        "packages": [
            {
            "name": "magma",
            "version": "0.0.0"
            }
        ],
        "vpn_ip": "10.0.0.1"
        },
        "system_status": {
        "cpu_idle": 0,
        "cpu_system": 0,
        "cpu_user": 0,
        "disk_partitions": [
            {
            "device": "/dev/sda1",
            "free": 15482871808,
            "mount_point": "/",
            "total": 21378641920,
            "used": 4809781248
            }
        ],
        "mem_available": 0,
        "mem_free": 0,
        "mem_total": 0,
        "mem_used": 0,
        "swap_free": 0,
        "swap_total": 0,
        "swap_used": 0,
        "time": 1234567000,
        "uptime_secs": 12345
        },
        "version": "string",
        "vpn_ip": "10.0.0.1"
    },
    "tier": "default"
    }
        return gateway_data
