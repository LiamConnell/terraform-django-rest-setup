
output "public_ip" {
  value = "${aws_instance.test_instance.public_ip}"
}

output "ansible_call" {
  value = "yes yes | ansible-playbook -u ubuntu -i '${self.public_ip},' --private-key ${var.ssh_key_private} provision.yml"
}
