import pytest
from triangle import can_form_triangle


class TestCanFormTriangle:
    """Test cases for the can_form_triangle function"""
    
    def test_valid_triangle_integers(self):
        """Test with valid triangle using integers"""
        assert can_form_triangle(3, 4, 5) == True
        assert can_form_triangle(5, 12, 13) == True
        assert can_form_triangle(1, 1, 1) == True
    
    def test_valid_triangle_floats(self):
        """Test with valid triangle using floating point numbers"""
        assert can_form_triangle(3.5, 4.2, 5.8) == True
        assert can_form_triangle(1.1, 1.1, 1.5) == True
        assert can_form_triangle(2.5, 3.0, 4.0) == True
    
    def test_invalid_triangle_inequality_violation(self):
        """Test cases that violate triangle inequality"""
        assert can_form_triangle(1, 2, 5) == False  # 1 + 2 < 5
        assert can_form_triangle(10, 1, 1) == False  # 1 + 1 < 10
        assert can_form_triangle(1, 10, 1) == False  # 1 + 1 < 10
    
    def test_edge_case_equal_to_sum(self):
        """Test edge case where sum of two sides equals the third"""
        assert can_form_triangle(1, 2, 3) == False  # 1 + 2 = 3
        assert can_form_triangle(5, 5, 10) == False  # 5 + 5 = 10
    
    def test_equilateral_triangle(self):
        """Test equilateral triangles"""
        assert can_form_triangle(5, 5, 5) == True
        assert can_form_triangle(2.5, 2.5, 2.5) == True
    
    def test_isosceles_triangle(self):
        """Test isosceles triangles"""
        assert can_form_triangle(5, 5, 8) == True
        assert can_form_triangle(3, 7, 7) == True
        assert can_form_triangle(10, 6, 10) == True
    
    def test_scalene_triangle(self):
        """Test scalene triangles"""
        assert can_form_triangle(3, 4, 5) == True
        assert can_form_triangle(6, 8, 10) == True
        assert can_form_triangle(5, 7, 9) == True
    
    def test_zero_values(self):
        """Test with zero values - should raise ValueError"""
        with pytest.raises(ValueError, match="All sides must be positive"):
            can_form_triangle(0, 4, 5)
        
        with pytest.raises(ValueError, match="All sides must be positive"):
            can_form_triangle(3, 0, 5)
        
        with pytest.raises(ValueError, match="All sides must be positive"):
            can_form_triangle(3, 4, 0)
    
    def test_negative_values(self):
        """Test with negative values - should raise ValueError"""
        with pytest.raises(ValueError, match="All sides must be positive"):
            can_form_triangle(-1, 4, 5)
        
        with pytest.raises(ValueError, match="All sides must be positive"):
            can_form_triangle(3, -2, 5)
        
        with pytest.raises(ValueError, match="All sides must be positive"):
            can_form_triangle(3, 4, -1)
    
    def test_non_numeric_values(self):
        """Test with non-numeric values - should raise TypeError"""
        with pytest.raises(TypeError, match="All sides must be numeric values"):
            can_form_triangle("3", 4, 5)
        
        with pytest.raises(TypeError, match="All sides must be numeric values"):
            can_form_triangle(3, "4", 5)
        
        with pytest.raises(TypeError, match="All sides must be numeric values"):
            can_form_triangle(3, 4, "5")
        
        with pytest.raises(TypeError, match="All sides must be numeric values"):
            can_form_triangle(None, 4, 5)
        
        with pytest.raises(TypeError, match="All sides must be numeric values"):
            can_form_triangle([3], 4, 5)
    
    def test_very_small_values(self):
        """Test with very small positive values"""
        assert can_form_triangle(0.001, 0.001, 0.001) == True
        assert can_form_triangle(0.1, 0.1, 0.15) == True
    
    def test_large_values(self):
        """Test with large values"""
        assert can_form_triangle(1000, 1000, 1000) == True
        assert can_form_triangle(999, 1000, 1001) == True
        assert can_form_triangle(1, 1000, 2000) == False


# Additional standalone test functions (alternative to class-based tests)
def test_basic_triangle():
    """Basic test for a simple valid triangle"""
    assert can_form_triangle(3, 4, 5) == True


def test_impossible_triangle():
    """Basic test for an impossible triangle"""
    assert can_form_triangle(1, 1, 5) == False


if __name__ == "__main__":
    # Run tests if this file is executed directly
    pytest.main([__file__])