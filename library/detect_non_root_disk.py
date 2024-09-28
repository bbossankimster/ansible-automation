from ansible.module_utils.basic import AnsibleModule


def main():
    args = dict(
            root_partion_disk=dict(required=True, type="str"),
            devices=dict(required=True, type="dict")
    )
    module = AnsibleModule(
        argument_spec=args,
        supports_check_mode=True
    )
    nonroot_disk = 'NOT_FOUND'
    ansible_devices = module.params.get('devices', {})
    root_partion_disk = module.params.get('root_partion_disk', 'ROOTDISK_NOT_FOUND').replace(r'"', '')
    for dev, dev_info in ansible_devices.items():
        if dev_info['scheduler_mode'] not in ['none', ''] and dev != root_partion_disk:
            nonroot_disk = dev
            break
    module.exit_json(changed=False, stdout=nonroot_disk)


if __name__ == '__main__':
    main()
