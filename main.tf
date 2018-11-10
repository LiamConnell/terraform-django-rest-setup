provider "aws" {
  region     = "us-west-2"
}


variable "ssh_key_private" {
  type = "string"
  default = "~/.ssh/liams_key.pem"
}
variable "instance_type" {
  type = "string"
  default = "t3.small"
}

variable "instance_name" {
  type = "string"
  default = "test_instance"
}



######################
### security group ###
######################

resource "aws_security_group" "allow_all" {
  description = "Allow all inbound traffic"
  ingress {
    from_port   = 0
    to_port     = 65535
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    from_port = 0
    to_port = 0
    protocol = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  tags {
    Name = "allow_all"
  }
}

###########
### EC2 ###
###########




resource "aws_instance" "${var.instance_type}" {
  ami           = "ami-0231c1de0d92fe7a2"
  instance_type = "${var.instance_type}"
  vpc_security_group_ids	= [
		"${aws_security_group.allow_all.id}"
			]
  key_name	= "liams_key"

  provisioner "remote-exec" {
    inline = ["sudo apt-get install python",
              ]
    connection {
      type        = "ssh"
      user        = "ubuntu"
      private_key = "${file(var.ssh_key_private)}"
    }
  }
  provisioner "local-exec" {
    command = "echo \"alias ssh_alias='ssh -i ${var.ssh_key_private} ubuntu@${self.public_ip}'\" > script.sh && source script.sh" # && rm -rf source.sh"
  }
  provisioner "local-exec" {
    command = "yes yes | ansible-playbook -u ubuntu -i '${self.public_ip},' --private-key ${var.ssh_key_private} provision.yml"
  }
}
