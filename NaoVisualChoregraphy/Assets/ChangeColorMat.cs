using UnityEngine;
using System.Collections;

public class ChangeColorMat : MonoBehaviour {
	private MeshRenderer mMeshRenderer;
	// Use this for initialization
	void Start () 
	{
		Color lMatColor = new Color (1f, 1f, 1f, 0.5f);
		mMeshRenderer = GetComponent<MeshRenderer> ();
		mMeshRenderer.materials [0].color = lMatColor;
	}
	
	// Update is called once per frame
	void Update () {
	
	}
}
