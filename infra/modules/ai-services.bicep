// AI Services Bicep module

@description('Location for all resources')
param location string

@description('Environment name')
param environment string

@description('Unique suffix for resource names')
param uniqueSuffix string

// Azure OpenAI
resource openai 'Microsoft.CognitiveServices/accounts@2023-05-01' = {
  name: 'openai-${environment}-${uniqueSuffix}'
  location: location
  kind: 'OpenAI'
  sku: {
    name: 'S0'
  }
  properties: {
    customSubDomainName: 'openai-${environment}-${uniqueSuffix}'
  }
}

// Outputs
output openaiEndpoint string = openai.properties.endpoint
