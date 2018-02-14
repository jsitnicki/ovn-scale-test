- Rally 0.10 has removed ServerProviders, that means that we can only have
  Deployment engines that use an existing deployment. We will have to move the
  deployment logic out of Rally plugin into, for example, Ansible playbooks that
  prepare the central and farm nodes.
