# ansible-role-system_role

## Description

Retern system role from network information

## Requirements

- ipaddress library

## Dependencies

None

## Role Variables:

### network(dict)

```
system_role_network:
  <rolename>:
    - <network>
    - <network>
```

## Example Playbook

````
- hosts: all
  gather_facts: true
  tasks:
    - name: call system role 
      system_role:
        network: "{{ system_role_network }}"
      register: system_role_output
    - debug:
        msg: "this host on home environment"
      when: system_role_output is defined and system_role_output['system_role'] == 'home_debian'
    - debug:
        msg: "this host on earth environment"
      when: system_role_output is defined and system_role_output['system_role'] == 'earth_debian'
    - debug:
        msg: "this host on moon environment"
      when: system_role_output is defined and system_role_output['system_role'] == 'moon_debian'
  roles:
    - system_role
````

## Example Vars

````
system_role_network:
  home:
    - '192.168.1.0/24'
  earth:
    - '192.168.2.0/24'
    - '172.18.48.0/20'
  moon:
    - '172.19.64.0/20'
````

## License

This role is under the MIT License. See the LICENSE file for the full license text.