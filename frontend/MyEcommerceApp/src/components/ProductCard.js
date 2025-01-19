import React from 'react';
import { View, Text, Image, StyleSheet } from 'react-native';

const ProductCard = ({ product }) => {
  return (
    <View style={styles.card}>
      <Image source={{ uri: product.image }} style={styles.image} />
      <Text style={styles.name}>{product.name}</Text>
      <Text style={styles.price}>${product.price}</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  card: {
    backgroundColor: '#FFF',
    padding: 10,
    borderRadius: 10,
    elevation: 2,
    margin: 10,
  },
  image: {
    width: '100%',
    height: 150,
    resizeMode: 'contain',
    borderRadius: 5,
  },
  name: {
    fontSize: 18,
    fontWeight: 'bold',
  },
  price: {
    color: 'green',
    fontSize: 16,
  },
});

export default ProductCard;
