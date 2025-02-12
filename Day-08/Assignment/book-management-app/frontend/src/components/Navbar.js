import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <nav className="navbar">
      <h2>📚 Book Manager</h2>
      <div>
        <Link to="/">Home</Link>
        <Link to="/create" className="btn">Add Book</Link>
      </div>
    </nav>
  );
};

export default Navbar;