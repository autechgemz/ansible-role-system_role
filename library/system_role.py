#!/usr/bin/python
import ipaddress
from ansible.module_utils.basic import AnsibleModule 
from ansible.module_utils.facts import ansible_facts 

DOCUMENTATION = r'''
module: system_role
short_description: Retern system role information
description:
  - Compare the IP address of the target from the information defined in the vars variable and print the role name.
requirements: ["Needed ipaddress library module"]
'''

EXAMPLES = r'''
- name: call system_role
    system_role:
      network: "{{ system_role_network }}"
    register: system_role_output
'''

def main():
    module = AnsibleModule(
        argument_spec=dict(
          network=dict(type='dict', required=True),
        ),
        supports_check_mode=True
    )

    network_param = module.params['network']

    all_facts = ansible_facts(module)
    os_family = all_facts.get('os_family').lower()
    addr_pool = all_facts.get('all_ipv4_addresses')

    roleset = None
    for role, nets in network_param.items():
        for net in nets:
            for addr in addr_pool:
                ip = ipaddress.ip_address(addr)
                nw = ipaddress.IPv4Network(net)
                if ip in list(nw):
                    roleset = role

    if roleset:
      output = roleset + '_' + os_family
    else:
      output = 'unknown' + '_' + os_family

    result = {
        'changed': False,
        'system_role': output,
    }
    module.exit_json(**result)

if __name__ == '__main__':
    main()
