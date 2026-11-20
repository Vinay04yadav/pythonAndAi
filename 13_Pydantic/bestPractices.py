# Model Organization
# 1. Define leaf models first - Models with no dependencies
# 2. Build upward - Gradually compose more complex models
# 3. Use clear naming - Make relationships obvious
# 4. Group related models - Keep models in logical modules

# Performance Considerations
# 1. Deep nesting impacts performance - keep reasonable depth
# 2. Large lists of nested models - consider pagination
# 3. Circular reference - Use carefully, can cause memory issues
# 4. Lazy loading - Consider for expensive nested computations

# Data modeling tips
# 1. Model real-world relationships - Mirror your domain structure
# 2. Use optional appropriately - Not all relationships are required
# 3. Consider Union types - For polymorphic relationships
# 4. Validate business rules - Use model validators for cross-model logic