import React from 'react';
import { View, Text, Image, StyleSheet, Button } from 'react-native';

const ProductDetailScreen = ({ route }) => {
  const { product } = route.params;

  return (
    <View style={styles.container}>
      <Image source={{ uri: product.image }} style={styles.image} />
      <Text style={styles.title}>{product.name}</Text>
      <Text>{product.description}</Text>
      <Text style={styles.price}>${product.price}</Text>
      <Button title="Add to Cart" onPress={() => {}} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
  },
  image: {
    width: '100%',
    height: 300,
    resizeMode: 'contain',
  },
  title: {
    fontSize: 22,
    fontWeight: 'bold',
  },
  price: {
    fontSize: 20,
    color: 'green',
  },
});

export default ProductDetailScreen;
