from rest_framework import serializers
from .models import SmartContract, Memory

class SmartContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmartContract
        fields = ['id', 'date', 'contract_address', 'ipfs_url']

class MemorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Memory
        fields = ['id', 'memory', 'ipfs_url']