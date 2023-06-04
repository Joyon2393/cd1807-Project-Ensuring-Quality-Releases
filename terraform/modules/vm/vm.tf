resource "azurerm_network_interface" "nic" {
  name                = "${var.application_type}-nic"
  location            = "${var.location}"
  resource_group_name = "${var.resource_group}"

  ip_configuration {
    name                          = "internal"
    subnet_id                     = "${var.subnet_id}"
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = "${var.public_ip_address_id}"
  }
}


resource "azurerm_linux_virtual_machine" "vm" {
  name                = "${var.application_type}-${var.resource_type}"
  location            = "${var.location}"
  resource_group_name = "${var.resource_group}"
  size                = "Standard_B1s"
  admin_username      = "azureuser"
  network_interface_ids = [azurerm_network_interface.nic.id]
  admin_ssh_key {
    username   = "azureuser"
    public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC0O9n1A5am5Qj2VK2cG6eTjkLGr7wxocMAv1x4gM7KhlivHxPOTka5NIkwKrHyRKcA23x3VdmbrfkhiQF3yJSxAO5Fegj0Qk9oQTx5k81w08tKXlqtquLNEEm3WtJQm7qIO1XfB1QELcxQjL/QWzhf1yzQUyZ/Y+nuwqMO2tsM5EcFa5U1OfTaMAdkWFC1HqonP3A+Fqopa+AMrNrzHiQzQLqdLtIzArZ+7mDa3sANIPUKBVFaRK4RpqaH/wTqiE1hEzaulylrRauS5UHfT8H0qQKmFNu9OQK+Wlc82zsi3RRmOr7pralFifFNlEI3resFQXsIfkWG0MKe/2oCpQmXKX8S+v8sIhzmWct7IS7KC4pDs+cY5/o+Mc+DQhbI/Dom+jL/haiDPRa9HywqY/fhU5h7DeYXvj9pELQ6QhXPp8kfQWrne61R0ZQUO6ew3ZJkikzr56njm0wd+zKUCDqsRhonVPYWcp0VCPHjp+H0Jfc7vyrQMBvHXHliF5ab3Yk= joyon@joyon-Personal"
  }
  os_disk {
    caching           = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }
  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "18.04-LTS"
    version   = "latest"
  }
}
