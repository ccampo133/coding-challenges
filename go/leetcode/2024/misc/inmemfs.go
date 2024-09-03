package misc

import (
	"slices"
	"strings"
)

// https://leetcode.com/problems/design-in-memory-file-system/description/
// Design a data structure that simulates an in-memory file system.
//
// Implement the FileSystem class:
//
// FileSystem() Initializes the object of the system.
// List<String> ls(String path)
// If path is a file path, returns a list that only contains this file's name.
// If path is a directory path, returns the list of file and directory names in
// this directory. The answer should in lexicographic order.
//
// void mkdir(String path): Makes a new directory according to the given path.
// The given directory path does not exist. If the middle directories in the
// path do not exist, you should create them as well.
//
// void addContentToFile(String filePath, String content)
// If filePath does not exist, creates that file containing given content.
// If filePath already exists, appends the given content to original content.
//
// String readContentFromFile(String filePath) Returns the content in the file at
// filePath.
//
// Example 1:
// Input
// ["FileSystem", "ls", "mkdir", "addContentToFile", "ls", "readContentFromFile"]
// [[], ["/"], ["/a/b/c"], ["/a/b/c/d", "hello"], ["/"], ["/a/b/c/d"]]
// Output
// [null, [], null, null, ["a"], "hello"]
//
// Explanation
// FileSystem fileSystem = new FileSystem();
// fileSystem.ls("/");                         // return []
// fileSystem.mkdir("/a/b/c");
// fileSystem.addContentToFile("/a/b/c/d", "hello");
// fileSystem.ls("/");                         // return ["a"]
// fileSystem.readContentFromFile("/a/b/c/d"); // return "hello"
//
//
// Constraints:
//
// 1 <= path.length, filePath.length <= 100
// path and filePath are absolute paths which begin with '/' and do not end with
// '/' except that the path is just "/".
// You can assume that all directory names and file names only contain lowercase
// letters, and the same names will not exist in the same directory.
// You can assume that all operations will be passed valid parameters, and users
// will not attempt to retrieve file content or list a directory or file that
// does not exist.
// 1 <= content.length <= 50
// At most 300 calls will be made to ls, mkdir, addContentToFile, and
// readContentFromFile.

// Node represents a filesystem node, based on a trie structure.
type Node struct {
	paths         map[string]*Node
	name, content string
	isFile        bool
}

// NewNode is the constructor for Node.
func NewNode(name string, isFile bool) *Node {
	return &Node{
		paths:  make(map[string]*Node),
		name:   name,
		isFile: isFile,
	}
}

// FileSystem represents an in-memory filesystem. Internally it uses a trie-like
// structure to represent the filesystem.
type FileSystem struct {
	root *Node
}

// Constructor initializes the filesystem.
func Constructor() FileSystem {
	fs := FileSystem{}
	fs.root = NewNode("", false)
	return fs
}

// Ls returns the names of the files and directories in the given path. If the
// path is a file, it returns a single-element slice containing the file's name.
func (fs *FileSystem) Ls(path string) []string {
	cur := fs.root
	ds := splitPath(path)
	for _, dir := range ds {
		cur = cur.paths[dir]
	}
	if cur.isFile {
		return []string{ds[len(ds)-1]}
	}
	paths := make([]string, 0, len(cur.paths))
	for name := range cur.paths {
		paths = append(paths, name)
	}
	slices.Sort(paths)
	return paths
}

// Mkdir creates a new directory at the given path.
func (fs *FileSystem) Mkdir(path string) {
	cur := fs.root
	for _, dir := range splitPath(path) {
		if _, ok := cur.paths[dir]; !ok {
			cur.paths[dir] = NewNode(dir, false)
		}
		cur = cur.paths[dir]
	}
}

// AddContentToFile adds content to the file at the given path. If the file does
// not exist, it creates it.
func (fs *FileSystem) AddContentToFile(filePath string, content string) {
	dirs := splitPath(filePath)
	// We don't go all the way to the end of the path because the problem
	// description says we can assume valid input. In that case, the last
	// element must be the file.
	cur := fs.root
	for _, dir := range dirs[:len(dirs)-1] {
		cur = cur.paths[dir]
	}
	fname := dirs[len(dirs)-1]
	file, ok := cur.paths[fname]
	// File does not exist - create it.
	if !ok {
		file = NewNode(fname, true)
		cur.paths[fname] = file
	}
	file.content += content
}

// ReadContentFromFile returns the content of the file at the given path.
func (fs *FileSystem) ReadContentFromFile(filePath string) string {
	cur := fs.root
	for _, dir := range splitPath(filePath) {
		cur = cur.paths[dir]
	}
	// We don't need to check if the current node is a file since the problem
	// description says we can assume valid input. That would be a good idea in
	// general though.
	return cur.content
}

func splitPath(path string) []string {
	if path == "/" {
		return []string{}
	}
	return strings.Split(path, "/")[1:]
}
